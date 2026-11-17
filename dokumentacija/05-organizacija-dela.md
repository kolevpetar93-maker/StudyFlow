# Načrt razvoja in odgovornosti

Delamo postopno: najprej dogovor in prototip, nato lokalni uporabniški tok, mobilne funkcije ter integracije. Konkretne datume dopolnimo, ko poznamo rok oddaje. Spodnje faze nimajo izmišljenih rokov ali že potrjenih osebnih dodelitev.

## Faze in meje zaključka

| Faza | Rezultat | Kdaj je zaključena |
| --- | --- | --- |
| M0 Zasnova in prva oddaja | Dokumentacija, DPU, mockupi, model, arhitektura, javni repo, začetni Issues, člani in CI | Vsa dokazila iz kontrolnega seznama so preverjena na GitHubu. |
| M1 Osnovni Flutter projekt | Delujoč začetni zaslon, navigacija, dogovorjeno upravljanje stanja | Ekipa lahko zažene aplikacijo; analyze in osnovni testi uspejo. |
| M2 Lokalni podatki | Predmeti, naloge, razpoložljivost in SQLite | Podatki preživijo ponovni zagon; ključni vnosi so preverjeni. |
| M3 Načrtovanje | Predlog načrta in ponovna razporeditev | Testi pokrijejo roke, prekrivanja, premalo časa in potrditev sprememb. |
| M4 Učenje na napravi | Pomodoro, napredek, obvestila in senzorji | Osrednji tok in zavrnjena dovoljenja so preverjeni na napravi. |
| M5 Računi in koledar | Firebase, sinhronizacija in Google Calendar | Preverjeni so delo brez povezave, ločitev računov, konflikt in ponovni uvoz. |
| M6 Napredne funkcije | OCR in AI kvizi po potrditvi obsega | Preverjene so napake OCR, popravek besedila in neveljaven odgovor AI. |
| M7 Zaključek | Celovit pregled, posodobljena dokumentacija in predstavitev | Zahteve in dokazila so pregledani, znane omejitve zapisane. |

## Področja dela

| Področje | Obseg odgovornosti | Odgovorna oseba |
| --- | --- | --- |
| Vmesnik in uporabniška izkušnja | Zasloni, navigacija, skupni gradniki, mockupi | Določimo skupaj med Nađo, Ljupko in Petrom. |
| Podatki in integracije | Modeli, SQLite, Firebase in koledar | Določimo skupaj med Nađo, Ljupko in Petrom. |
| Načrtovanje in mobilne funkcije | Algoritem, Pomodoro, obvestila, senzorji | Določimo skupaj med Nađo, Ljupko in Petrom. |
| Dokumentacija in preverjanje | README, Issues, CI in pregled oddaje | Skupna odgovornost; vsaka naloga dobi enega nosilca. |

Po uporabnikovem dogovoru so vabila in objava Issues odloženi. Pred oddajo vsaki začetni nalogi dodelimo konkretnega člana in to tabelo nadomestimo s potrjenimi dodelitvami. Imena vloge niso dokaz že dodeljene naloge.

## Preprost potek dela

1. Iz [seznama nalog](07-zacetne-naloge.md) izberemo majhno nalogo in določimo nosilca, prioriteto ter merila sprejema.
2. Ustvarimo vejo, na primer `feature/predmeti` ali `docs/podatkovni-model`.
3. Spremembo izvedemo, preverimo in posodobimo povezano dokumentacijo.
4. Odprimo pull request; drug član pregleda spremembo in CI.
5. Po pregledu združimo v `main`, zapremo Issue in posodobimo stanje faze.

Pravila so podrobneje v [CONTRIBUTING](../CONTRIBUTING.md). Dokler dela samo en član, sam pregleda spremembe in zabeleži preverjanje; pregled drugega člana uvedemo po njegovem vključevanju.

## Prioritete in statusi

- **P1:** nujno za trenutno fazo ali blokira druge naloge.
- **P2:** naslednje funkcionalnosti po stabilnem jedru.
- **P3:** napredne funkcije po preverjanju izvedljivosti.

Statusi: **Backlog → Ready → In progress → Review → Done**. Naloga je Done, ko izpolni merila sprejema, ima potrebna preverjanja in posodobljeno dokumentacijo. Če rok ogroža obseg, to zapišemo in se dogovorimo o prilagoditvi; funkcij ne odstranjujemo tiho.
