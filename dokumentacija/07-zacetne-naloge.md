# Osnutki začetnih GitHub Issues

Po dogovoru z uporabnikom nalog še ne objavljamo. Spodaj so pripravljeni naslovi, opisi, prioritete, področja in merila sprejema. Pri objavi dodamo konkretnega odgovornega člana in oznake `P1`, `P2` ali `P3` ter področje. **Nedodeljeno** pomeni, da odgovorna oseba še ni potrjena.

## SF-01 Pregled projektne zasnove in mockupov

**Prioriteta:** P1. **Faza:** M0. **Področje:** dokumentacija. **Odgovorna oseba:** Nedodeljeno.

Ekipa pregleda zahteve F01–F13, DPU, scenarije, model in predlagane zaslone ter zapiše dogovor o obsegu.

**Merila sprejema:**

- [ ] Vsi člani pregledajo dokumentacijo in zapišejo pripombe.
- [ ] Potrjene in odprte odločitve so jasno ločene.
- [ ] Dokumentacija in mockupi imajo usklajene pojme in navigacijo.

**Odvisnosti:** brez.

## SF-02 Objaviti javni repozitorij in preveriti CI

**Prioriteta:** P1. **Faza:** M0. **Področje:** repozitorij. **Odgovorna oseba:** Nedodeljeno.

Objaviti pripravljeno strukturo na GitHubu in preveriti prvi workflow za oddani commit.

**Merila sprejema:**

- [ ] Repozitorij je javen in README vsebuje njegovo povezavo.
- [ ] Workflow uspe na GitHubu; v dokumentacijo je dodana povezava do izvajanja.
- [ ] Diagrami in lokalne povezave so pregledani tudi na GitHubu.

**Odvisnosti:** pripravljena lokalna struktura.

## SF-03 Dodati sodelujoče in razdeliti delo

**Prioriteta:** P1. **Faza:** M0. **Področje:** organizacija. **Odgovorna oseba:** Nedodeljeno.

Dodati Nađo, Ljupko in asistenta; preveriti dostop Petrovega računa. Objaviti začetne naloge in dogovoriti nosilce.

**Merila sprejema:**

- [ ] Znani so GitHub računi vseh zahtevanih sodelujočih in vabila so sprejeta.
- [ ] Začetni Issues imajo opis, prioriteto in odgovornega člana.
- [ ] Tabela odgovornosti in kontrolni seznam sta posodobljena.

**Odvisnosti:** SF-02; ta korak je za zdaj odložen po dogovoru z uporabnikom.

## SF-04 Inicializirati Flutter projekt in navigacijo

**Prioriteta:** P1. **Faza:** M1. **Področje:** vmesnik. **Odgovorna oseba:** Nedodeljeno.

Inicializirati projekt v korenu, ohraniti dokumentacijo, potrditi Riverpod ali Provider in povezati osnovne zaslone iz prototipa.

**Merila sprejema:**

- [ ] Aplikacija se zažene na dogovorjeni napravi ali emulatorju.
- [ ] Deluje prehod med Danes, Predmeti, Načrt in Napredek.
- [ ] README vsebuje dejansko preverjen SDK in ukaze; CI dobi analyze in smiselne prve teste.

**Odvisnosti:** SF-01.

## SF-05 Implementirati lokalne predmete, naloge in razpoložljivost

**Prioriteta:** P1. **Faza:** M2. **Področje:** podatki. **Odgovorna oseba:** Nedodeljeno.

Izdelati modele in SQLite shranjevanje za F01–F03 ter osnovne obrazce.

**Merila sprejema:**

- [ ] Podatki ostanejo po ponovnem zagonu aplikacije.
- [ ] Neveljavni vnosi imajo razumljiva sporočila; izbris pojasni posledice.
- [ ] Shranjevanje in datumske izjeme imajo preverjanja, ki pokrivajo dejanske napake.

**Odvisnosti:** SF-04.

## SF-06 Implementirati načrtovanje in prilagajanje

**Prioriteta:** P1. **Faza:** M3. **Področje:** načrtovanje. **Odgovorna oseba:** Nedodeljeno.

Razviti ločen algoritem za F04–F05 in prikaz predloga, primerjave ter potrditve.

**Merila sprejema:**

- [ ] Načrt nima prekrivanj ter upošteva roke in prosti čas.
- [ ] Premalo časa pokaže nerazporejeno delo.
- [ ] Potrditev spremeni le prihodnje neopravljene seje; zavrnitev ohrani stari načrt.
- [ ] Testi pokrijejo zamudo, spremembo trajanja, časovni pas in pomanjkanje prostih terminov.

**Odvisnosti:** SF-05.

## SF-07 Dodati Pomodoro in pregled napredka

**Prioriteta:** P2. **Faza:** M4. **Področje:** učenje. **Odgovorna oseba:** Nedodeljeno.

Izvesti F06–F07: seje, premor, zaključek, beleženje dejanskega časa in grafe iz shranjenih podatkov.

**Merila sprejema:**

- [ ] Ponovni zaključek ne podvoji zapisa časa.
- [ ] Vrnitev po prekinitvi pravilno obnovi stanje seje.
- [ ] Statistika izhaja iz podatkov, dokončanost naloge pa potrdi uporabnik.

**Odvisnosti:** SF-05; povezava z načrtom po SF-06.

## SF-08 Dodati lokalne opomnike in Focus Mode

**Prioriteta:** P2. **Faza:** M4. **Področje:** mobilne-funkcije. **Odgovorna oseba:** Nedodeljeno.

Izvesti F08–F09 in preveriti dovoljenja ter akcelerometer na napravi.

**Merila sprejema:**

- [ ] Zavrnitev obvestil ohrani uporabnost aplikacije.
- [ ] Sprememba ali izbris seje posodobi opomnik.
- [ ] Focus Mode je izbiren, ima ročni način in preverjeno vedenje med aktivno uporabo aplikacije.

**Odvisnosti:** SF-06 in SF-07.

## SF-09 Dodati Firebase račun in sinhronizacijo

**Prioriteta:** P2. **Faza:** M5. **Področje:** integracije. **Odgovorna oseba:** Nedodeljeno.

Izvesti F10, ločitev računov, obdelavo konfliktov in pravila dostopa.

**Merila sprejema:**

- [ ] Delo brez interneta ostane lokalno in se pozneje sinhronizira.
- [ ] Konflikt in menjava računa ne prepišeta ali pomešata podatkov.
- [ ] Pravila dostopa so preverjena; skrivnosti niso v repozitoriju.

**Odvisnosti:** SF-05 in dogovor o sinhronizaciji.

## SF-10 Povezati Google Calendar

**Prioriteta:** P2. **Faza:** M5. **Področje:** integracije. **Odgovorna oseba:** Nedodeljeno.

Izvesti F11: izbira koledarjev, uvoz zasedenih terminov in upoštevanje pri načrtovanju.

**Merila sprejema:**

- [ ] Ponovni uvoz ne podvoji dogodkov.
- [ ] Upoštevani so časovni pasovi in celodnevni dogodki.
- [ ] Zavrnitev dovoljenja ali napaka omrežja omogočata ročno nadaljevanje.

**Odvisnosti:** SF-06 in dogovor o OAuth konfiguraciji.

## SF-11 Preveriti izvedljivost in dodati OCR

**Prioriteta:** P3. **Faza:** M6. **Področje:** napredne-funkcije. **Odgovorna oseba:** Nedodeljeno.

Preveriti jezike in kakovost prepoznavanja ter izvesti F12 po potrditvi obsega.

**Merila sprejema:**

- [ ] Zapisane so dejansko preverjene omejitve, vključno z rokopisom.
- [ ] Uporabnik popravi besedilo in čas pred vključitvijo v načrt.
- [ ] Slika ne odide v oblak brez dogovorjenega in potrjenega toka.

**Odvisnosti:** SF-05 in SF-06.

## SF-12 Preveriti izvedljivost in dodati AI kvize

**Prioriteta:** P3. **Faza:** M6. **Področje:** napredne-funkcije. **Odgovorna oseba:** Nedodeljeno.

Izbrati ponudnika in zaščiteno zaledje ter izvesti F13 po potrditvi obsega.

**Merila sprejema:**

- [ ] Uporabnik potrdi pošiljanje izbranega besedila.
- [ ] Ključ je na zaledju, odgovor je preverjen in AI vsebina označena.
- [ ] Napake, neveljaven odgovor in omejitev zahtev imajo razumljivo obravnavo.

**Odvisnosti:** SF-09; uporabnik lahko besedilo vnese ročno, OCR ni obvezen predpogoj.
