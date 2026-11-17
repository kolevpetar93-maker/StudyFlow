# Razvoj in GitHub

## Trenutna struktura kode

| Pot | Namen |
| --- | --- |
| `lib/main.dart` | Vstopna točka in minimalna osnova aplikacije. |
| `lib/screens/` | Rezervirano za prihodnje zaslone; trenutno brez datotek Dart. |
| `lib/models/` | Prihodnji podatkovni modeli. |
| `lib/services/` | Prihodnje shranjevanje, načrtovanje in integracije. |
| `lib/providers/` | Prihodnje upravljanje stanja; knjižnico še izberemo. |
| `lib/widgets/` | Prihodnji skupni gradniki. |
| `assets/` | Prostor za statične datoteke aplikacije. |
| `test/app_test.dart` | Osnovno preverjanje zagona aplikacije. |
| `dokumentacija/` | Vsa projektna dokumentacija in mockupi. |

Posameznih zaslonov in navigacije še ne razvijamo. Mockupi so ločeni predlogi za pogovor v ekipi. `.gitkeep` ohrani prazne mape v Gitu.

## Lokalno preverjanje

Osnova uporablja Flutter **3.47.7** in Dart **3.13.5**. V korenu projekta:

```sh
flutter pub get
dart format --output=none --set-exit-if-changed lib test
flutter analyze
flutter test
python scripts/check_project.py
```

Python 3.12 ali novejši preveri dokumentacijo brez dodatnih paketov. Platformne mape `android` in `ios` dodamo, ko začnemo izvajanje na napravi; trenutna osnova omogoča analizo in widget test brez njih. Za Flutter osnove in teste uporabljamo [uradno dokumentacijo](https://docs.flutter.dev/learn/pathway) ter [navodila za testiranje](https://docs.flutter.dev/testing/overview).

## Sodelovanje

Za nalogo določimo nosilca in odpremo vejo, npr. `feature/predmeti`. Naredimo majhno spremembo, zaženemo preverjanja in odpremo pull request. Drug član pregleda rezultat pred združitvijo v `main`; do vključitve ekipe spremembe pregleda trenutni sodelujoči. Dokumentacijo posodobimo skupaj s kodo.

## Javna objava

Lokalni Git repozitorij že obstaja. Uporabnik ustvari prazen **javen** repozitorij `StudyFlow` na svojem GitHub profilu. Spremembe najprej shrani s commitom, nato poveže dejanski URL:

```sh
git add .
git commit -m "chore: update StudyFlow project setup"
git remote add origin https://github.com/VAS_GITHUB_RACUN/StudyFlow.git
git push -u origin main
```

`VAS_GITHUB_RACUN` zamenjajte z dejanskim računom. Če `origin` že obstaja, preverite `git remote -v` in ga ne dodajajte drugič. Vabila članom in asistentu ter Issues uredimo pozneje, pred oddajo.

## CI

[StudyFlow CI](../.github/workflows/ci.yml) preveri dokumentacijo, oblikovanje Dart kode, analizo in zagonski test. Po objavi odpremo Actions ter zabeležimo povezavo do uspešnega izvajanja za oddani commit. Workflow ne gradi APK ali iOS aplikacije.

Viri nastavitev: [checkout](https://github.com/actions/checkout), [setup-python](https://github.com/actions/setup-python), [flutter-action](https://github.com/subosito/flutter-action). Prijavni žetoni, AI ključi in zasebni uporabniški podatki ostanejo zunaj repozitorija.
