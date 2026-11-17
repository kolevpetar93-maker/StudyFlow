# Projektna zasnova StudyFlow

## Namen

StudyFlow je načrtovana mobilna aplikacija za študente in dijake. Rešuje težavo razporejanja učenja ob več predmetih, rokih in omejenem času. Uporabnik vnese obveznosti in razpoložljivost, aplikacija predlaga načrt ter ob zamudah ponudi novo razporeditev. Uporabnik spremembe pregleda in potrdi.

## Funkcionalne zahteve

| ID | Funkcionalnost | Osnovno merilo sprejema |
| --- | --- | --- |
| F01 | Dodajanje, urejanje in brisanje predmetov | Predmet je shranjen tudi po ponovnem zagonu; brisanje zahteva potrditev in pojasni vpliv na povezane podatke. |
| F02 | Naloge, izpiti in kolokviji | Vsaka obveznost ima predmet, naslov, rok, pozitivno trajanje, zahtevnost 1–5 in prioriteto 1–3. |
| F03 | Razpoložljivi termini učenja | Uporabnik določi tedenske termine in izjeme za posamezne dneve. |
| F04 | Dnevni in tedenski učni načrt | Seje se ne prekrivajo, upoštevajo prosti čas in roke; nerazporejeno delo je jasno prikazano. |
| F05 | Prilagajanje načrta | Zamuda ali sprememba trajanja ustvari predlog; prihodnje seje se spremenijo šele po potrditvi, pretekle opravljene ostanejo. |
| F06 | Pomodoro in beleženje časa | Uporabnik začne, ustavi in zaključi sejo; zapis časa se ne podvoji. Dokončanost naloge potrdi ločeno. |
| F07 | Napredek in statistika | Prikaz minut učenja, dokončanih nalog in napredka pri predmetih temelji na shranjenih podatkih. |
| F08 | Lokalna obvestila | Opomniki za roke in seje se ob prestavitvi ali izbrisu posodobijo; zavrnitev dovoljenja ne blokira aplikacije. |
| F09 | Focus Mode in akcelerometer | Med aktivno uporabo aplikacije je mogoče zaznati telefon z zaslonom navzdol; funkcija je izbirna in ima ročni način. |
| F10 | Računi in sinhronizacija | Firebase omogoči prijavo in prenos podatkov med napravami; lokalno delo je možno brez interneta. |
| F11 | Google Calendar | Uvoz zasedenih terminov upošteva dovoljenje uporabnika; ponovni uvoz ne podvoji dogodkov. |
| F12 | Kamera in OCR gradiva | Uporabnik lahko popravi prepoznano besedilo in oceno časa, preden nastanejo učne seje. |
| F13 | AI kvizi | Uporabnik potrdi pošiljanje besedila; odgovor ima preverjeno strukturo in je označen kot AI vsebina. |

## Predlagani vrstni red razvoja

1. **Lokalno jedro:** F01–F07, tok predmet → obveznost → razpoložljivost → načrt → seja → napredek.
2. **Mobilne funkcije:** F08–F09, obvestila in Focus Mode na fizični napravi.
3. **Integracije:** F10–F11, račun, sinhronizacija in Google Calendar.
4. **Napredne funkcije:** F12–F13, OCR in AI kvizi.

To je vrstni red, ne izključitev funkcij iz prvotnega predloga. Končni obseg naprednih funkcionalnosti uskladimo glede na zahteve predmeta in razpoložljivi čas. Prva oddaja vsebuje dokumentacijo in prototip; izvedba teh funkcij sledi pozneje.

## Nefunkcionalne zahteve

- Lokalni podatki in osnovno načrtovanje so uporabni brez povezave.
- Vnos ima jasne napake, prazni zasloni navodila, barva pa ni edina oznaka stanja.
- Trajanje je v minutah, časovni trenutki v UTC; prikaz in razpoložljivost upoštevata uporabnikov časovni pas.
- Dovoljenja za kamero, senzorje, koledar in obvestila se zahtevajo ob uporabi funkcije, z ročno alternativo kjer je mogoče.
- Skrivnosti AI ponudnika so na zaledju. Osebni koledarji, učno gradivo in žetoni ne sodijo v repozitorij ali dnevniške izpise.
- Algoritem načrtovanja je ločen od zaslonov, da ga lahko preverjamo na zamudah, prekrivanjih in premalo časa.
- Prva predlagana testna platforma je Android. iOS ostaja v načrtu; njegovo preverjanje potrebuje ustrezno okolje in napravo.

## Odprte odločitve

Ekipa pred implementacijo potrdi različice Flutter SDK in paketov, Riverpod ali Provider, pravila prioritet, sinhronizacijo in AI ponudnika. Preveriti moramo OCR za izbrane jezike in rokopis. Ocena časa učenja je približna in jo uporabnik vedno lahko spremeni.

Vsebinsko izhodišče je `OpisProjekta(3).docx`, »Predlog projektne naloge – StudyFlow«, RVIR 2026/2027. Merila sprejema in razdelitev v faze so začetni izvedbeni predlog.
