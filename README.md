# Zastosowania informatyki w gospodarce projekt

## Terminy

- [x] 1.03: 4 grupy
- [x] 8.03: temat, zakres tematyczny
- [x] 15.03: specyfikacja (funkcjonalność,  kamienie milowe)
- [ ] 29.03: Uzupełnienie wiedzy
- [ ] 19.04- I kamień milowy
- [ ] 17.05 – II kamień milowy
- [ ] 7.06 – III kamień milowy
- [ ] 14.06 – prezentacja rezultatów projektu, uwagi do kodu
- [ ] 21.06 – uzupełnienia dokumentacji i kodu


## Temat, zakres tematyczny

G. Rozpoznawanie języka migowego


- aplikacja webowa z obsługą kamery, wysyłająca wykonane przez użytkownika zdjęcia na serwer backendowy, 
- serwer backendowy rozpoznający gesty w języku migowym na otrzymanych zdjęciach i wysyłający informacje o rozpoznanym geście (REST API)


## Specyfikacja (funkcjonalność, kamienie milowe)

### Aplikacje webowa (frontendowa)

- Obsługa kamery
- Wysyłanie wykonanych zdjęć do usługi rozpoznającej zdjęcia
- Wyświetlanie wyników (rozpoznane znaki)

#### Technologie

- VueJS ?

### Serwer backendowy

- Przyjmowanie obrazów (z aplikacji webowej)
- Usługi rozpoznającej obrazy
- Zwrócenie wyniku rozpoznawania
- Komunikacja za pomocą REST API

#### Technologie

- FastAPI

### Usługa rozpoznająca obrazy

- Przyjmuje obraz
- Zwraca rozpoznany znak

#### Technologie

- YoloML ?
- Keras ?

# 

### Kamienie milowe

#### Pierwszy

- Zbudowanie datasetu (wyciągnięcie danych z google drive i ułożenie ich w format przystępny dla biblioteki MLkowej)

- Bootstrap projektu webowego z obsługą kamery

- Bootstrap projektu backendowego z przykładowym API


#### Drugi

- Rozpoznawanie znaków z datasetu, sprawność przynajmniej 20%

- Wysyłanie zdjęć przez API, wyświetlanie wyników

- Mockup api przetwarzającego zdjęcia i wysyłającego wyniki


#### Trzeci

- Usprawnienie dokładności rozpoznawania znaków

    - Rozszerzenie datasetu
    - Przetestowanie metod wstępnej filtracji obrazu (OpenCV)
    - Przetestowanie różnych modeli rozpoznających obrazy

- Responsywna strona internetowa aplikacji

- Rate limiting (?), przetwarzanie w jakiejś kolejce dunno
