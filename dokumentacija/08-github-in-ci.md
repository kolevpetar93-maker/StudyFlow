# Objava na GitHubu in prvi CI

## Kaj je pripravljeno

Lokalna struktura, README, dokumentacija, predloga naloge in workflow so pripravljeni za prvi javni repozitorij. Uporabnik bo objavo izvedel sam; vabila in Issues bomo uredili pozneje. Ne ustvarjamo dodatnih računov ali storitev.

## Objava

1. Na GitHubu ustvarite **javen** repozitorij `StudyFlow`. Ne dodajte novega README, licence ali `.gitignore`, ker začetne datoteke že obstajajo lokalno. Licenco izberemo skupaj pozneje.
2. Če lokalni repozitorij še ni inicializiran, v korenski mapi izvedite spodnje ukaze. Če že obstaja, najprej preverite `git status` in preskočite že izvedene korake.

```sh
git init -b main
git add .
git commit -m "docs: initial StudyFlow planning and prototype"
```

3. Kopirajte HTTPS URL svojega novega repozitorija. V naslednjem primeru zamenjajte `VAS_GITHUB_RACUN` z dejanskim uporabniškim imenom, nato izvedite:

```sh
git remote add origin https://github.com/VAS_GITHUB_RACUN/StudyFlow.git
git push -u origin main
```

Če `origin` že obstaja, preverite `git remote -v` in uporabite pravi cilj; ne dodajajte ga drugič. Če je `main` že objavljen, nadaljnje spremembe shranite z novim commitom in običajnim pushom.

4. V README dodajte dejanski URL. V zavihku Actions odprite izvajanje **StudyFlow CI** in preverite zelen rezultat za oddani commit.
5. V to dokumentacijo dodajte povezavo do uspešnega izvajanja. Do takrat ne označimo GitHub CI kot preverjenega.

Alternativa ob prijavljenem GitHub CLI: `gh repo create StudyFlow --public --source=. --remote=origin --push`. Uporabite jo samo, če ciljni repozitorij in remote še ne obstajata.

## Sodelujoči in naloge pozneje

- V nastavitvah repozitorija dodajte račune članov in asistenta; preverite sprejeta vabila.
- V Issues prenesite začetne naloge iz [osnutkov](07-zacetne-naloge.md). Dodajte konkretne assignee in oznake `P1`, `P2`, `P3` ter področje.
- V [organizaciji dela](05-organizacija-dela.md) zapišite potrjene osebne odgovornosti.
- Posodobite [kontrolni seznam](00-nacrt-oddaje.md). Ti koraki so za zdaj odloženi, za končno oddajo pa zahtevani.

## Kaj preverja CI

[Workflow](../.github/workflows/ci.yml) se izvede ob vsakem pushu, pull requestu in ročnem zagonu. Z dovoljenjem samo za branje prenese repozitorij, pripravi Python in zažene [preverjanje](../scripts/check_project.py).

Preverjanje zahteva osnovne dokumente in Flutter mape, preveri lokalne povezave v Markdownu in HTML, veljavnost SVG ter obstoj ciljev navigacije prototipa. Preveri tudi, da osnutki nalog vsebujejo prioriteto, odgovornost in merila sprejema. Ne preverja zunanjih povezav, dejanske prijave, senzorjev, sinhronizacije ali Flutter kode.

Uporabljena sta uradna [actions/checkout](https://github.com/actions/checkout) in [actions/setup-python](https://github.com/actions/setup-python). Ob inicializaciji Flutter aplikacije dodamo preverjene različice orodij, `flutter analyze` in smiselne teste dejanske kode.
