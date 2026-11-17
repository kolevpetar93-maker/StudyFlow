# Osnovne Flutter mape

Za zdaj so pripravljene samo mape. Projekt še nima `pubspec.yaml`, `main.dart` ali platformnih map, zato ukaza `flutter run` še ne moremo uporabiti.

| Mapa | Kaj bo v njej | Primer prihodnje datoteke |
| --- | --- | --- |
| `screens/` | Zasloni aplikacije | `home_screen.dart` |
| `models/` | Podatkovni modeli | `subject.dart`, `task.dart` |
| `services/` | SQLite, načrtovanje, Firebase in povezave s storitvami | `planning_service.dart` |
| `providers/` | Upravljanje stanja zaslonov | `tasks_provider.dart` |
| `widgets/` | Manjši skupni gradniki | `task_card.dart` |

Primeri datotek še niso implementirani. `providers` je ime mape; izbira Riverpod ali Provider še ni dokončna.

Ob začetku razvoja inicializiramo Flutter projekt v korenu repozitorija. Pred tem naredimo commit, nato pregledamo ustvarjene datoteke in ohranimo ta README ter dokumentacijo. SDK in ukaze zabeležimo takrat, ko jih dejansko preverimo.
