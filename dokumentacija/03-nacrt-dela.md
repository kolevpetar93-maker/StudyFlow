# Načrt dela

## Faze

| Faza | Rezultat |
| --- | --- |
| 1 Zasnova in oddaja | Dokumentacija, DPU, mockupi, javni repo, člani, začetni Issues in uspešen CI. |
| 2 Lokalno jedro | Predmeti, obveznosti, razpoložljivost in SQLite. Zaslone oblikujemo skupaj ob začetku te faze. |
| 3 Učni načrt | Izdelava predloga in potrjena prerazporeditev; testi rokov, prekrivanj in premalo časa. |
| 4 Učenje na napravi | Pomodoro, napredek, lokalni opomniki in Focus Mode. |
| 5 Integracije | Firebase računi, sinhronizacija in Google Calendar. |
| 6 Napredne funkcije | OCR in AI kvizi po preverjanju izvedljivosti ter potrditvi obsega. |

Datume dopolnimo po dogovoru o rokih. Po vsaki fazi preverimo rezultat in posodobimo dokumentacijo.

## Odgovornosti

Ekipo sestavljajo Nađa Tomović, Ljupka Koteska in Petar Kolev. Osebno razdelitev potrdimo skupaj pred objavo Issues. Vsaka naloga dobi enega odgovornega člana in po možnosti drugega za pregled.

| Področje | Delo | Nosilec |
| --- | --- | --- |
| Vmesnik | Zasloni, navigacija in skupni gradniki | Še določimo |
| Podatki | Modeli, SQLite, Firebase in koledar | Še določimo |
| Načrtovanje | Algoritem, Pomodoro in mobilne funkcije | Še določimo |
| Dokumentacija in preverjanje | README, naloge, CI in pregled oddaje | Vsi; nosilec po nalogi |

## Osnutki začetnih Issues

P1 = nujno za trenutno fazo, P2 = naslednje funkcije, P3 = napredne funkcije. Objavo in osebno dodelitev smo po dogovoru odložili; spodnja tabela ju ne nadomesti.

| ID | Naloga in pričakovani rezultat | Prioriteta | Odgovorni član |
| --- | --- | --- | --- |
| SF-01 | Pregledati zasnovo, dodati DPU in potrditi mockupe; dokumentacija je usklajena. | P1 | Nedodeljeno |
| SF-02 | Objaviti javni repo; povezava in uspešen CI sta zabeležena. | P1 | Nedodeljeno |
| SF-03 | Dodati člane in asistenta, objaviti Issues ter potrditi odgovornosti. | P1 | Nedodeljeno |
| SF-04 | Razviti lokalne predmete, naloge in razpoložljivost; podatki ostanejo po ponovnem zagonu. | P1 | Nedodeljeno |
| SF-05 | Razviti načrtovanje; brez prekrivanj, opozorilo ob premalo časa, spremembe po potrditvi. | P1 | Nedodeljeno |
| SF-06 | Dodati Pomodoro, statistiko, opomnike in senzorje; preverjeno tudi z zavrnjenimi dovoljenji. | P2 | Nedodeljeno |
| SF-07 | Dodati Firebase in koledar; preveriti delo brez interneta, konflikte in ponovni uvoz. | P2 | Nedodeljeno |
| SF-08 | Preveriti in dodati OCR ter AI; omogočiti popravek besedila in varno obravnavo napak. | P3 | Nedodeljeno |

Pri objavi večje naloge razdelimo na manjše Issues z opisom, odvisnostmi in merili sprejema. Potek: **Backlog → In progress → Review → Done**. V vejo `main` združimo pregledano spremembo z uspešnimi preverjanji.
