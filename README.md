# First small fastapi assignment

### Ogólnie
W tym zadaniu należy przygotować serwis RESTowy w oparciu o fastAPI, zaprezentować automatyczną dokumentację tego serwisu oraz przetestować go za pomocą curla.

### Zadania
* Zaimplementuj end-point listujący wszystkie tagi wraz z liczbą obrazków przypisanych do danego tagu. End-point powinien być dostępny pod ścieżką /tags.
* Zaimplementuj end-point listujący wszystkie obrazki wraz z ich tagami. End-point powinien być dostępny pod ścieżką /images.
* Zaimplementuj end-point listujący wszystkie obrazki przypisane do danego tagu. End-point powinien być dostępny pod ścieżką /images/{tag}.
* Zaimplementuj end-point kasujący obrazki. End-point powinien być dostępny pod ścieżką /images/del. Identyfikatory obrazków do skasowania powinny być przekazane w formie JSONa.
