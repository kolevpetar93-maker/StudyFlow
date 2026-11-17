# Projektna zasnova

## Namen

StudyFlow pomaga študentom in dijakom uskladiti več predmetov, rokov in učnih nalog. Uporabnik vnese obveznosti in prosti čas, aplikacija pa predlaga učni načrt. Ob zamudah ali spremenjenem trajanju ponudi novo razporeditev, ki jo uporabnik potrdi.

## Glavne funkcionalnosti

| Funkcionalnost | Pričakovano vedenje |
| --- | --- |
| Predmeti in obveznosti | Dodajanje, urejanje in brisanje predmetov, izpitov, kolokvijev in nalog; rok, zahtevnost, prioriteta in ocena časa. |
| Načrtovanje | Dnevni in tedenski predlog brez prekrivanj, glede na roke in razpoložljivost. Premalo časa se prikaže kot opozorilo. |
| Prilagajanje načrta | Ob zamudi predlog novih prihodnjih terminov; opravljene seje ostanejo ohranjene. |
| Pomodoro in Focus Mode | Učni intervali z odmori, dejanski čas učenja ter izbirno zaznavanje telefona z zaslonom navzdol med aktivno uporabo. |
| Opomniki in napredek | Lokalna obvestila, dokončane naloge in statistika po predmetih. |
| Računi in koledar | Firebase prijava in sinhronizacija; uvoz zasedenih terminov iz Google Calendar. |
| OCR | Zajem gradiva, popravek prepoznanega besedila ter prilagodljiva ocena časa in razdelitev v seje. |
| AI kvizi | Kratki kvizi iz uporabnikovega besedila; napredna funkcija po preverjanju izvedljivosti. |

## Ključni uporabniški scenariji

| Cilj | Potek | Rezultat |
| --- | --- | --- |
| Dodati obveznost | Uporabnik izbere predmet, vnese naslov, vrsto, rok in trajanje ter shrani. | Obveznost je na seznamu. Napačni vnosi imajo razumljivo sporočilo. |
| Izdelati načrt | Določi razpoložljivost, zahteva predlog in ga potrdi. | Seje upoštevajo roke in zasedenost; nerazporejeno delo je vidno. |
| Nadomestiti zamujeno sejo | Označi zamudo, pregleda novi termin in potrdi ali zavrne. | Spremeni se samo potrjeno prihodnje delo. |
| Opraviti učenje | Začne Pomodoro, po potrebi ustavi in zaključi; ločeno označi opravljeno nalogo. | Shrani se dejanski čas brez podvojitve. |
| Uporabiti integracije | Po želji poveže račun ali koledar in dovoli dostop. | Sinhronizacija oziroma uvoz; brez dovoljenja ostane ročna lokalna uporaba. |
| Uporabiti gradivo | Zajame sliko, popravi OCR in čas; po potrditvi pošlje izbrano besedilo za kviz. | Gradivo je povezano z nalogo; napake OCR in AI omogočajo popravek oziroma ponovni poskus. |

## Osnovna pravila

- Jedro aplikacije je uporabno brez interneta; integracije jasno pokažejo napake.
- Uporabnik potrdi spremembe načrta, dovoljenja in pošiljanje besedila AI storitvi.
- Statistika temelji na shranjenih podatkih; čas učenja sam po sebi ne zaključi naloge.
- OCR ocena časa je približna. Podporo jezikom in rokopisu preverimo pred implementacijo.
- Osebnih koledarjev, gradiva in prijavnih podatkov ne dodajamo v repozitorij.

Izhodišče: posredovani predlog `OpisProjekta(3).docx`. Končni obseg naprednih funkcij prilagodimo zahtevam predmeta in času; začetna koda še ne izvaja teh funkcionalnosti.
