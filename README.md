# NetworkSniffer

NetworkSniffer je nástroj pro zachytávání, monitorování a analýzu síťového provozu. Umožňuje sledovat komunikaci zařízení, zaznamenávat informace o síťových paketech a odhalovat podezřelé chování či anomálie v síti. Později bude součástí projektu Qubitac.

- Získávání IP adres, portů, protokolů a DNS dotazů.
- Seskupování paketů do jednotlivých komunikací (flows).
- Ukládání informací do SQLite.
- Detekce podezřelých intervalů komunikace a dalších anomálií.
- Zjišťování přibližné geografické polohy IP adres.
- Poskytování dat přes lokální REST API.
- Příprava na propojení s Avalonia UI projektu Qubitac (přehledné zobrazování výsledků analýz).

## 2. Struktura projektu

| Soubor | Odpovědnost |
|---|---|
| `main.py` | Spuštění a propojení všech modulů |
| `config.py` | Konfigurace snifferu a nastavení |
| `capture.py` | Zachytávání paketů pomocí Scapy |
| `parser.py` | Extrakce informací z paketů |
| `flows.py` | Seskupování paketů a počítání statistik |
| `analyzer.py` | Analýza provozu a detekce anomálií |
| `database.py` | Práce s SQLite databází |
| `api.py` | REST API pro externí aplikace |
| `requirements.txt` | Seznam potřebných knihoven |
| `data/` | Lokální databáze a další data |

## 3. Průběh zpracování

1. `capture.py` zachytává pakety z vlastního PC nebo sítě (hub, port mirroring, gateway apod.).
2. `parser.py` převede paket na strukturovaná data.
3. `flows.py` přiřadí paket k odpovídající komunikaci.
4. `analyzer.py` vyhodnotí případné anomálie.
5. `database.py` uloží výsledky do SQLite.
6. `api.py` umožní ostatním aplikacím získat uložené informace.

## 4. Plán vývoje

### Fáze 1 – Základní zachytávání

- Nainstalovat Scapy a Npcap.
- Implementovat `capture.py`.
- Implementovat `parser.py`.
- Vypisovat zachycené pakety do konzole.

### Fáze 2 – Databáze a komunikace

- Vytvořit SQLite databázi.
- Ukládat informace o zachycené komunikaci.
- Implementovat `flows.py`.
- Zaznamenávat počty paketů, bajty a časové údaje.

### Fáze 3 – Analýza

- Implementovat detekci pravidelných intervalů komunikace.
- Detekovat neobvyklé množství provozu.
- Přidat GeoIP.
- Ukládat upozornění do databáze.

### Fáze 4 – API

- Implementovat FastAPI.
- Endpoint pro historii komunikace.
- Endpoint pro statistiky.
- Endpoint pro upozornění.
- Připravit rozhraní pro Avalonia UI.

## 5. Zásady projektu

- Každý soubor má jednu hlavní odpovědnost.
- Moduly by měly být co nejméně závislé na sobě.
- Zachytávání paketů nesmí blokovat ukládání do databáze.
- Neuchovávat zbytečně kompletní obsah všech paketů.
- API bude ve výchozím nastavení dostupné pouze lokálně.
- Projekt bude možné později provozovat na Raspberry Pi.

**Verze:** 0.1.0
