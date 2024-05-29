# Python dla inżynierów - skrypt uzupełniający

## Składnia i podstawowe instrukcje.

### Składnia i podstawowe instrukcje w Pythonie

Python to wysokopoziomowy język programowania, który jest znany ze swojej czytelności i prostoty składni. Dzięki temu, jest często wybierany jako pierwszy język programowania. W tej sekcji omówimy podstawowe elementy składni Pythona oraz kilka fundamentalnych instrukcji, które są niezbędne do tworzenia programów.

#### 1. Komentarze

Komentarze są nie wykonywane przez program i służą do opisywania kodu. W Pythonie są oznaczane znakiem `#`.

```python
# To jest komentarz
print("Hello, World!")  # To również jest komentarz
```

#### 2. Zmienne i typy danych

Python jest językiem dynamicznie typowanym, co oznacza, że nie trzeba deklarować typu zmiennej. Poniżej przedstawiamy kilka podstawowych typów danych.

```python
# Liczby całkowite
a = 5

# Liczby zmiennoprzecinkowe
b = 3.14

# Ciągi znaków (stringi)
c = "Hello"

# Wartości logiczne (booleany)
d = True
```

#### 3. Operatory

Operatory służą do wykonywania operacji na zmiennych i wartościach.

```python
# Operatory arytmetyczne
x = 10
y = 3
print(x + y)  # Dodawanie
print(x - y)  # Odejmowanie
print(x * y)  # Mnożenie
print(x / y)  # Dzielenie
print(x // y) # Dzielenie całkowite
print(x % y)  # Reszta z dzielenia
print(x ** y) # Potęgowanie

# Operatory porównania
print(x == y) # Równość
print(x != y) # Nierówność
print(x > y)  # Większe
print(x < y)  # Mniejsze
print(x >= y) # Większe lub równe
print(x <= y) # Mniejsze lub równe

# Operatory logiczne
print(x > 5 and y < 5) # AND
print(x > 5 or y < 2)  # OR
print(not(x > 5))      # NOT
```

#### 4. Instrukcje warunkowe

Instrukcje warunkowe pozwalają na wykonywanie różnych bloków kodu w zależności od spełnienia określonych warunków.

```python
a = 10
if a > 5:
    print("a jest większe od 5")
elif a == 5:
    print("a jest równe 5")
else:
    print("a jest mniejsze od 5")
```

#### 5. Pętle

Pętle służą do wykonywania określonego bloku kodu wielokrotnie.

```python
# Pętla while
i = 0
while i < 5:
    print(i)
    i += 1

# Pętla for
for i in range(5):
    print(i)
```

#### 6. Funkcje

Funkcje pozwalają na definiowanie bloków kodu, które mogą być wielokrotnie używane.

```python
def przywitaj(imie):
    return f"Cześć, {imie}!"

print(przywitaj("Jan"))
```

#### 7. Listy

Listy są jednym z podstawowych typów danych służących do przechowywania sekwencji elementów.

```python
lista = [1, 2, 3, 4, 5]
print(lista[0])  # Dostęp do pierwszego elementu
print(lista[-1]) # Dostęp do ostatniego elementu
lista.append(6)  # Dodanie elementu na końcu listy
print(lista)
```

### Przykład

Poniżej znajduje się prosty program, który demonstruje powyższe elementy składni i instrukcji w Pythonie:

```python
def oblicz_sume(lista):
    suma = 0
    for liczba in lista:
        suma += liczba
    return suma

liczby = [1, 2, 3, 4, 5]
wynik = oblicz_sume(liczby)
print(f"Suma liczb w liście to: {wynik}")
```

Ten program definiuje funkcję `oblicz_sume`, która oblicza sumę liczb w liście, a następnie używa tej funkcji do obliczenia sumy elementów w liście `liczby` i wypisuje wynik.

W kolejnych krokach możemy rozwinąć ten program, dodając bardziej zaawansowane funkcje i struktury danych, ale te podstawy są fundamentem, na którym opiera się cały język Python.

## Konfiguracja środowiska do wygodnego programowania w Pythonie (IDE)

### Konfiguracja środowiska do wygodnego programowania w Pythonie (IDE)

Python to wszechstronny język programowania, który można używać do różnych celów, od analizy danych po tworzenie aplikacji internetowych. Aby skutecznie pracować w Pythonie, warto skonfigurować odpowiednie środowisko programistyczne (IDE). W tej sekcji omówimy najpopularniejsze IDE dla Pythona oraz kroki konfiguracji środowiska pracy.

#### 1. Wybór IDE

Wybór odpowiedniego IDE zależy od osobistych preferencji oraz rodzaju projektów, nad którymi będziesz pracować. Poniżej przedstawiamy kilka popularnych opcji:

- **PyCharm**: Rozbudowane IDE oferujące wiele funkcji, takich jak debugowanie, analiza kodu, refaktoryzacja i wsparcie dla frameworków.
- **Visual Studio Code (VS Code)**: Lekki edytor kodu z wieloma rozszerzeniami, w tym wsparciem dla Pythona.
- **Jupyter Notebook**: Świetne narzędzie do interaktywnej pracy z kodem, szczególnie popularne w analizie danych i uczeniu maszynowym.
- **Spyder**: IDE skierowane do naukowców i inżynierów, z wbudowanym wsparciem dla analiz danych i tworzenia wizualizacji.
- **IDLE**: Proste IDE dostarczane razem z Pythonem, dobre dla początkujących.

#### 2. Instalacja Pythona

Przed rozpoczęciem pracy w wybranym IDE, musisz zainstalować Pythona. Możesz pobrać najnowszą wersję z oficjalnej strony [python.org](https://www.python.org/downloads/). Upewnij się, że podczas instalacji zaznaczysz opcję dodania Pythona do zmiennej środowiskowej PATH.

#### 3. Konfiguracja PyCharm

1. **Pobierz i zainstaluj PyCharm**: Możesz pobrać PyCharm z [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/download/).
2. **Utwórz nowy projekt**: Po uruchomieniu PyCharm, wybierz opcję utworzenia nowego projektu. Wybierz lokalizację i nazwę projektu.
3. **Skonfiguruj interpreter Pythona**: W sekcji "New Project" wybierz interpreter Pythona, który został zainstalowany na Twoim komputerze.
4. **Instalacja dodatkowych bibliotek**: Możesz zainstalować dodatkowe biblioteki, takie jak numpy, pandas czy matplotlib, korzystając z wbudowanego menedżera pakietów.

#### 4. Konfiguracja Visual Studio Code (VS Code)

1. **Pobierz i zainstaluj VS Code**: Możesz pobrać VS Code z [code.visualstudio.com](https://code.visualstudio.com/Download).
2. **Zainstaluj rozszerzenie Python**: Otwórz VS Code i przejdź do zakładki "Extensions" (rozszerzenia). Wyszukaj i zainstaluj rozszerzenie Python.
3. **Skonfiguruj interpreter Pythona**: Otwórz plik .py, a następnie wybierz odpowiedni interpreter Pythona z listy sugerowanej przez VS Code.
4. **Instalacja dodatkowych bibliotek**: W terminalu wbudowanym w VS Code użyj pip, aby zainstalować potrzebne biblioteki, np. `pip install numpy`.

#### 5. Konfiguracja Jupyter Notebook

1. **Instalacja Jupyter Notebook**: Możesz zainstalować Jupyter Notebook za pomocą pip:
   ```bash
   pip install notebook
   ```
2. **Uruchomienie Jupyter Notebook**: W terminalu wpisz:
   ```bash
   jupyter notebook
   ```
   Otworzy to interfejs Jupyter Notebook w przeglądarce.
3. **Tworzenie nowego notebooka**: Wybierz opcję "New" i stwórz nowy notebook Python 3.

#### 6. Konfiguracja Spyder

1. **Pobierz i zainstaluj Anaconda**: Anaconda to dystrybucja Pythona, która zawiera Spyder oraz wiele przydatnych bibliotek. Pobierz ją z [anaconda.com](https://www.anaconda.com/products/individual).
2. **Uruchomienie Spyder**: Po instalacji, otwórz Anaconda Navigator i uruchom Spyder.

#### 7. Konfiguracja IDLE

1. **IDLE jest dostarczane razem z Pythonem**: Jeśli zainstalowałeś Pythona, IDLE powinno być już dostępne. Możesz je znaleźć w menu Start lub uruchomić, wpisując `idle` w terminalu.

### Podsumowanie

Konfiguracja środowiska programistycznego dla Pythona jest kluczowym krokiem do efektywnego programowania. Wybór odpowiedniego IDE zależy od Twoich potrzeb i preferencji. Każde z opisanych narzędzi oferuje różne funkcje, które mogą wspomóc Twój proces tworzenia i debugowania kodu.

Jeśli masz pytania dotyczące konkretnej konfiguracji lub potrzebujesz pomocy w rozwiązaniu problemów, nie wahaj się pytać!

## Różne sposoby uruchamiania programów w Pythonie (Windows / Linux).

### Różne sposoby uruchamiania programów w Pythonie (Windows / Linux)

Python jest językiem wszechstronnym, który można uruchamiać na różnych systemach operacyjnych, takich jak Windows i Linux. W tej sekcji omówimy różne metody uruchamiania programów w Pythonie na tych systemach.

#### 1. Uruchamianie programów w Pythonie z poziomu terminala (Windows / Linux)

Najprostszym sposobem uruchomienia programu w Pythonie jest użycie terminala lub wiersza poleceń.

**Windows:**

1. Otwórz Wiersz Poleceń (Command Prompt). Możesz to zrobić, wpisując `cmd` w pasku wyszukiwania i klikając na "Wiersz Poleceń".
2. Przejdź do katalogu, w którym znajduje się Twój skrypt Pythona, używając komendy `cd`:
   ```shell
   cd ścieżka/do/twojego/katalogu
   ```
3. Uruchom skrypt Pythona, wpisując:
   ```shell
   python nazwa_pliku.py
   ```

**Linux:**

1. Otwórz Terminal. Możesz to zrobić, naciskając `Ctrl + Alt + T` lub szukając "Terminal" w menu aplikacji.
2. Przejdź do katalogu, w którym znajduje się Twój skrypt Pythona, używając komendy `cd`:
   ```shell
   cd /ścieżka/do/twojego/katalogu
   ```
3. Uruchom skrypt Pythona, wpisując:
   ```shell
   python3 nazwa_pliku.py
   ```

#### 2. Uruchamianie programów w Pythonie z poziomu IDE (Windows / Linux)

Wiele IDE umożliwia uruchamianie skryptów Pythona bezpośrednio z ich interfejsu.

**PyCharm:**

1. Otwórz projekt w PyCharm.
2. Kliknij prawym przyciskiem myszy na plik `.py`, który chcesz uruchomić, i wybierz "Run 'nazwa_pliku'".
3. Wynik zostanie wyświetlony w dolnym oknie terminala PyCharm.

**Visual Studio Code (VS Code):**

1. Otwórz plik `.py` w VS Code.
2. Kliknij na ikonę odtwarzania (▶) w prawym górnym rogu edytora, aby uruchomić skrypt.
3. Wynik zostanie wyświetlony w wbudowanym terminalu VS Code.

**Jupyter Notebook:**

1. Otwórz notebook w Jupyter.
2. Kliknij na komórkę z kodem, który chcesz uruchomić, i naciśnij `Shift + Enter` lub kliknij na ikonę odtwarzania (▶).

#### 3. Uruchamianie programów Pythona jako skrypty wykonywalne (Linux)

Na systemach Linux można uruchamiać skrypty Pythona bezpośrednio jako pliki wykonywalne.

1. Dodaj shebang na początku pliku `.py`:
   ```python
   #!/usr/bin/env python3
   ```
2. Nadaj plikowi prawa do wykonywania:
   ```shell
   chmod +x nazwa_pliku.py
   ```
3. Uruchom skrypt bezpośrednio:
   ```shell
   ./nazwa_pliku.py
   ```

#### 4. Uruchamianie programów Pythona z poziomu menedżerów pakietów (Windows / Linux)

Niektóre programy Pythona są dystrybuowane jako pakiety i można je uruchamiać za pomocą menedżerów pakietów, takich jak `pip`.

1. Zainstaluj pakiet za pomocą `pip`:
   ```shell
   pip install nazwa_pakietu
   ```
2. Uruchom program zainstalowany jako pakiet:
   ```shell
   nazwa_pakietu
   ```

#### 5. Uruchamianie programów Pythona jako usługi systemowe (Linux)

Na systemach Linux można skonfigurować skrypty Pythona jako usługi systemowe.

1. Utwórz plik jednostki systemd w `/etc/systemd/system/`:
   ```ini
   [Unit]
   Description=Moja aplikacja Python

   [Service]
   ExecStart=/usr/bin/python3 /ścieżka/do/skryptu/nazwa_pliku.py
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```
2. Zrestartuj demon systemd:
   ```shell
   sudo systemctl daemon-reload
   ```
3. Uruchom usługę:
   ```shell
   sudo systemctl start nazwa_usługi
   ```
4. Aby włączyć usługę przy starcie systemu:
   ```shell
   sudo systemctl enable nazwa_usługi
   ```

### Podsumowanie

Uruchamianie programów Pythona może być realizowane na wiele sposobów, w zależności od systemu operacyjnego i preferencji użytkownika. Wybór metody zależy od kontekstu użycia, a umiejętność korzystania z różnych metod daje elastyczność i pozwala na efektywne zarządzanie projektami Pythona.

Jeśli masz pytania dotyczące konkretnych metod uruchamiania skryptów lub potrzebujesz dodatkowych wyjaśnień, nie wahaj się pytać!


## Rozpowszechnianie swoich programów,


### Rozpowszechnianie swoich programów w Pythonie

Rozpowszechnianie programów napisanych w Pythonie może być realizowane na wiele różnych sposobów, w zależności od potrzeb i środowiska docelowego. Poniżej omówimy kilka metod dystrybucji programów Pythona, w tym tworzenie pakietów, używanie wirtualnych środowisk, tworzenie instalatorów oraz dystrybucję kodu źródłowego.

#### 1. Tworzenie pakietów i dystrybucja przez PyPI

**PyPI (Python Package Index)** to repozytorium, które umożliwia udostępnianie pakietów Python, dzięki czemu inne osoby mogą je łatwo zainstalować za pomocą narzędzia `pip`.

**Kroki do stworzenia i opublikowania pakietu na PyPI:**

1. **Utwórz strukturę katalogów projektu:**

   ```
   my_package/
   ├── my_package/
   │   ├── __init__.py
   │   └── my_module.py
   ├── tests/
   │   └── test_my_module.py
   ├── setup.py
   ├── README.md
   └── LICENSE
   ```

2. **Zdefiniuj plik `setup.py`:**

   ```python
   from setuptools import setup, find_packages

   setup(
       name='my_package',
       version='0.1.0',
       packages=find_packages(),
       install_requires=[
           'numpy',  # przykładowa zależność
       ],
       entry_points={
           'console_scripts': [
               'my_command=my_package.my_module:main_function',
           ],
       },
       author='Twoje Imię',
       author_email='twojemail@example.com',
       description='Opis twojego pakietu',
       long_description=open('README.md').read(),
       long_description_content_type='text/markdown',
       url='https://github.com/twoj_github/my_package',
       classifiers=[
           'Programming Language :: Python :: 3',
           'License :: OSI Approved :: MIT License',
           'Operating System :: OS Independent',
       ],
       python_requires='>=3.6',
   )
   ```

3. **Utwórz i opublikuj pakiet:**

   ```shell
   pip install --upgrade setuptools wheel twine
   python setup.py sdist bdist_wheel
   twine upload dist/*
   ```

#### 2. Dystrybucja kodu źródłowego

Kod źródłowy można dystrybuować za pośrednictwem platform takich jak GitHub, GitLab czy Bitbucket.

**Kroki do udostępnienia kodu na GitHubie:**

1. **Utwórz repozytorium na GitHubie.**
2. **Zainicjuj repozytorium w lokalnym katalogu projektu:**

   ```shell
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/twoj_github/my_package.git
   git push -u origin master
   ```

#### 3. Tworzenie wirtualnych środowisk

Tworzenie wirtualnych środowisk umożliwia separację zależności dla różnych projektów. Jest to szczególnie przydatne przy dystrybucji programów, ponieważ można łatwo zainstalować wszystkie wymagane biblioteki w izolowanym środowisku.

**Kroki do stworzenia wirtualnego środowiska:**

1. **Utwórz wirtualne środowisko:**

   ```shell
   python -m venv myenv
   ```

2. **Aktywuj wirtualne środowisko:**

   **Windows:**

   ```shell
   myenv\Scripts\activate
   ```

   **Linux/Mac:**

   ```shell
   source myenv/bin/activate
   ```

3. **Zainstaluj zależności:**

   ```shell
   pip install -r requirements.txt
   ```

#### 4. Tworzenie instalatorów (Windows)

Tworzenie instalatorów dla systemu Windows umożliwia łatwą instalację programów przez użytkowników końcowych.

**Kroki do stworzenia instalatora przy użyciu PyInstaller:**

1. **Zainstaluj PyInstaller:**

   ```shell
   pip install pyinstaller
   ```

2. **Utwórz plik wykonywalny:**

   ```shell
   pyinstaller --onefile my_script.py
   ```

   To polecenie utworzy plik wykonywalny w katalogu `dist`.

#### 5. Tworzenie kontenerów Docker

Konteneryzacja aplikacji za pomocą Dockera umożliwia łatwe uruchamianie aplikacji w różnych środowiskach.

**Kroki do utworzenia obrazu Docker:**

1. **Utwórz plik `Dockerfile`:**

   ```Dockerfile
   FROM python:3.8-slim

   WORKDIR /app
   COPY . /app

   RUN pip install --no-cache-dir -r requirements.txt

   CMD ["python", "my_script.py"]
   ```

2. **Zbuduj obraz Docker:**

   ```shell
   docker build -t my_image .
   ```

3. **Uruchom kontener:**

   ```shell
   docker run -it my_image
   ```

### Podsumowanie

Rozpowszechnianie programów Pythona może być realizowane na różne sposoby, w zależności od potrzeb i środowiska docelowego. Możesz wybierać między publikacją pakietów na PyPI, udostępnianiem kodu źródłowego, tworzeniem wirtualnych środowisk, tworzeniem instalatorów dla systemu Windows lub konteneryzacją aplikacji za pomocą Dockera.

Każda z tych metod ma swoje zalety i wady, a wybór odpowiedniej zależy od Twoich specyficznych potrzeb oraz odbiorców Twojego programu. Jeśli masz pytania dotyczące konkretnej metody dystrybucji lub potrzebujesz dodatkowych wyjaśnień, nie wahaj się pytać!

### PyPi test

Publikacja pakietu na Test PyPI (https://test.pypi.org/) pozwala na przetestowanie procesu publikacji bez ryzyka wpływu na produkcyjne PyPI. Poniżej znajdują się kroki, które należy wykonać, aby opublikować pakiet na Test PyPI.

#### 1. Utworzenie konta na Test PyPI

1. Przejdź na stronę [Test PyPI](https://test.pypi.org/).
2. Utwórz nowe konto lub zaloguj się, jeśli już masz konto.

#### 2. Przygotowanie projektu

Przygotuj strukturę katalogów projektu i plik `setup.py`, jak opisano wcześniej.

**Przykład struktury projektu:**

```
my_package/
├── my_package/
│   ├── __init__.py
│   └── my_module.py
├── tests/
│   └── test_my_module.py
├── setup.py
├── README.md
└── LICENSE
```

**Przykładowy plik `setup.py`:**

```python
from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',  # przykładowa zależność
    ],
    entry_points={
        'console_scripts': [
            'my_command=my_package.my_module:main_function',
        ],
    },
    author='Twoje Imię',
    author_email='twojemail@example.com',
    description='Opis twojego pakietu',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/twoj_github/my_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
```

#### 3. Utworzenie pakietu

1. **Zainstaluj wymagane narzędzia:**

   ```shell
   pip install --upgrade setuptools wheel twine
   ```

2. **Utwórz dystrybucję pakietu:**

   ```shell
   python setup.py sdist bdist_wheel
   ```

   To polecenie utworzy pliki w katalogu `dist/`.

#### 4. Publikacja pakietu na Test PyPI

1. **Prześlij pakiet na Test PyPI za pomocą `twine`:**

   ```shell
   twine upload --repository-url https://test.pypi.org/legacy/ dist/*
   ```

2. **Podaj swoje poświadczenia (nazwa użytkownika i hasło) do Test PyPI, gdy zostaniesz o to poproszony.**

#### 5. Instalacja pakietu z Test PyPI

Aby upewnić się, że pakiet został poprawnie opublikowany, możesz spróbować go zainstalować z Test PyPI w nowym środowisku wirtualnym.

1. **Utwórz nowe środowisko wirtualne:**

   ```shell
   python -m venv test_env
   ```

2. **Aktywuj środowisko wirtualne:**

   **Windows:**

   ```shell
   test_env\Scripts\activate
   ```

   **Linux/Mac:**

   ```shell
   source test_env/bin/activate
   ```

3. **Zainstaluj pakiet z Test PyPI:**

   ```shell
   pip install --index-url https://test.pypi.org/simple/ my_package
   ```

### Podsumowanie

Publikacja pakietu na Test PyPI jest świetnym sposobem na przetestowanie procesu dystrybucji i instalacji pakietu przed opublikowaniem go na produkcyjnym PyPI. Postępując zgodnie z powyższymi krokami, możesz upewnić się, że Twój pakiet jest prawidłowo przygotowany i że proces publikacji przebiega bez problemów. 

Jeśli napotkasz jakiekolwiek problemy lub masz pytania dotyczące poszczególnych kroków, nie wahaj się pytać!


## Tworzenie wersji nie wymagającej zainstalowanego Pythona

### Tworzenie wersji programu Python nie wymagającej zainstalowanego Pythona

Tworzenie wersji programu w Pythonie, która nie wymaga zainstalowanego środowiska Python na komputerze użytkownika, można zrealizować na kilka sposobów. Najpopularniejsze narzędzia do tego celu to PyInstaller, cx_Freeze i py2exe. W tym artykule skupimy się na PyInstallerze, ponieważ jest on szeroko stosowany i dobrze udokumentowany.

#### PyInstaller

**PyInstaller** pozwala na stworzenie samodzielnych plików wykonywalnych z aplikacji Pythona. Te pliki zawierają wszystkie potrzebne zależności, co umożliwia uruchomienie aplikacji na komputerze bez zainstalowanego Pythona.

##### Kroki do stworzenia pliku wykonywalnego za pomocą PyInstaller:

1. **Zainstaluj PyInstaller:**

   Użyj `pip` do zainstalowania PyInstaller:

   ```shell
   pip install pyinstaller
   ```

2. **Przygotuj swój skrypt Python:**

   Upewnij się, że Twój skrypt Python działa poprawnie. Na potrzeby tego przykładu, załóżmy, że Twój plik nazywa się `main.py`.

3. **Utwórz plik wykonywalny:**

   W terminalu, przejdź do katalogu zawierającego `main.py` i uruchom PyInstaller:

   ```shell
   pyinstaller --onefile main.py
   ```

   - Opcja `--onefile` spowoduje, że PyInstaller utworzy jeden plik wykonywalny. Możesz również użyć opcji `--noconsole` jeśli nie chcesz, aby konsola była wyświetlana (dla aplikacji GUI).

4. **Zlokalizuj wygenerowany plik:**

   Po zakończeniu procesu, PyInstaller utworzy katalog `dist` w bieżącym katalogu. Plik wykonywalny będzie się znajdował w środku tego katalogu.

##### Konfiguracja spec pliku (opcjonalnie):

PyInstaller generuje plik `.spec`, który zawiera konfigurację budowania. Możesz edytować ten plik, aby dostosować proces tworzenia pliku wykonywalnego.

1. **Otwórz plik `.spec`:**

   Plik `.spec` będzie miał nazwę zgodną z Twoim skryptem Python, np. `main.spec`.

2. **Dostosuj plik `.spec`:**

   Możesz zmieniać różne opcje, takie jak dodawanie dodatkowych plików, zmiana nazwy pliku wykonywalnego, itp.

   **Przykład dodawania dodatkowych plików:**

   ```python
   a = Analysis(['main.py'],
                pathex=['/ścieżka/do/katalogu'],
                binaries=[],
                datas=[('additional_file.txt', 'dest_folder')],
                hiddenimports=[],
                hookspath=[],
                runtime_hooks=[],
                excludes=[],
                win_no_prefer_redirects=False,
                win_private_assemblies=False,
                cipher=block_cipher)
   ```

3. **Zbuduj ponownie plik wykonywalny:**

   Użyj PyInstaller z plikiem `.spec`:

   ```shell
   pyinstaller main.spec
   ```

### Alternatywne narzędzia

#### cx_Freeze

**cx_Freeze** to kolejne narzędzie do tworzenia plików wykonywalnych z aplikacji Pythona.

1. **Zainstaluj cx_Freeze:**

   ```shell
   pip install cx_Freeze
   ```

2. **Utwórz plik `setup.py`:**

   ```python
   from cx_Freeze import setup, Executable

   setup(
       name = "MyApp",
       version = "0.1",
       description = "My Python application!",
       executables = [Executable("main.py")],
   )
   ```

3. **Utwórz plik wykonywalny:**

   ```shell
   python setup.py build
   ```

#### py2exe

**py2exe** to narzędzie specyficzne dla systemu Windows.

1. **Zainstaluj py2exe:**

   ```shell
   pip install py2exe
   ```

2. **Utwórz plik `setup.py`:**

   ```python
   from distutils.core import setup
   import py2exe

   setup(console=['main.py'])
   ```

3. **Utwórz plik wykonywalny:**

   ```shell
   python setup.py py2exe
   ```

### Podsumowanie

Tworzenie samodzielnych plików wykonywalnych z aplikacji Python może być łatwo zrealizowane za pomocą narzędzi takich jak PyInstaller, cx_Freeze lub py2exe. Każde z tych narzędzi ma swoje zalety i może być używane w różnych sytuacjach w zależności od potrzeb projektu. PyInstaller jest często wybierany ze względu na swoją prostotę i szeroką funkcjonalność.

Jeśli masz pytania dotyczące konkretnego narzędzia lub procesu tworzenia pliku wykonywalnego, nie wahaj się pytać!

## Obsługa opcji podanych programowi z linii poleceń (argparse i alternatywy)

W Pythonie istnieje kilka bibliotek, które umożliwiają łatwe przetwarzanie argumentów przekazywanych z linii poleceń. Najbardziej popularną biblioteką do tego celu jest `argparse`, która jest wbudowana w standardową bibliotekę Pythona. Istnieją także alternatywy, takie jak `click` i `docopt`. W tym artykule omówimy podstawowe użycie `argparse` oraz krótkie wprowadzenie do `click` i `docopt`.

#### argparse

Biblioteka `argparse` jest częścią standardowej biblioteki Pythona i pozwala na definiowanie, przetwarzanie i dokumentowanie argumentów linii poleceń w prosty sposób.

**Przykład użycia `argparse`:**

1. **Podstawowy skrypt z `argparse`:**

   ```python
   import argparse

   def main():
       parser = argparse.ArgumentParser(description="Opis twojego programu")
       parser.add_argument("nazwa_pliku", type=str, help="Nazwa pliku do przetworzenia")
       parser.add_argument("--liczba", type=int, help="Opcjonalna liczba", default=10)
       parser.add_argument("--verbose", action="store_true", help="Włącz tryb szczegółowy")

       args = parser.parse_args()

       if args.verbose:
           print(f"Przetwarzam plik {args.nazwa_pliku} z opcjonalną liczbą {args.liczba}")

       # Reszta kodu twojego programu
       print(f"Nazwa pliku: {args.nazwa_pliku}")
       print(f"Liczba: {args.liczba}")

   if __name__ == "__main__":
       main()
   ```

   **Jak uruchomić:**

   ```shell
   python main.py example.txt --liczba 42 --verbose
   ```

2. **Zaawansowane funkcje `argparse`:**

   `argparse` oferuje wiele zaawansowanych funkcji, takich jak grupowanie argumentów, parsowanie podpoleceń i obsługa plików konfiguracyjnych.

   **Przykład z grupowaniem argumentów:**

   ```python
   import argparse

   def main():
       parser = argparse.ArgumentParser(description="Program do przetwarzania danych")

       group = parser.add_mutually_exclusive_group(required=True)
       group.add_argument("--sum", action="store_true", help="Suma liczb")
       group.add_argument("--prod", action="store_true", help="Iloczyn liczb")

       parser.add_argument("num1", type=int, help="Pierwsza liczba")
       parser.add_argument("num2", type=int, help="Druga liczba")

       args = parser.parse_args()

       if args.sum:
           result = args.num1 + args.num2
       elif args.prod:
           result = args.num1 * args.num2

       print(f"Wynik: {result}")

   if __name__ == "__main__":
       main()
   ```

   **Jak uruchomić:**

   ```shell
   python main.py 5 3 --sum
   python main.py 5 3 --prod
   ```

#### click

Biblioteka `click` jest nowoczesną alternatywą dla `argparse`, zaprojektowaną z myślą o łatwiejszym definiowaniu interfejsów wiersza poleceń. Oferuje bardziej zwięzły kod i wiele zaawansowanych funkcji.

1. **Podstawowy skrypt z `click`:**

   ```python
   import click

   @click.command()
   @click.argument('nazwa_pliku')
   @click.option('--liczba', default=10, help='Opcjonalna liczba')
   @click.option('--verbose', is_flag=True, help='Włącz tryb szczegółowy')
   def main(nazwa_pliku, liczba, verbose):
       if verbose:
           click.echo(f"Przetwarzam plik {nazwa_pliku} z opcjonalną liczbą {liczba}")

       click.echo(f"Nazwa pliku: {nazwa_pliku}")
       click.echo(f"Liczba: {liczba}")

   if __name__ == "__main__":
       main()
   ```

   **Jak uruchomić:**

   ```shell
   python main.py example.txt --liczba 42 --verbose
   ```

#### docopt

`docopt` to biblioteka, która automatycznie generuje interfejsy wiersza poleceń na podstawie dokumentacji.

1. **Podstawowy skrypt z `docopt`:**

   ```python
   """Program do przetwarzania danych.

   Użycie:
     main.py <nazwa_pliku> [--liczba=<int>] [--verbose]

   Opcje:
     --liczba=<int>  Opcjonalna liczba [domyślnie: 10].
     --verbose       Włącz tryb szczegółowy.
   """

   from docopt import docopt

   def main():
       args = docopt(__doc__)
       nazwa_pliku = args['<nazwa_pliku>']
       liczba = int(args['--liczba'])
       verbose = args['--verbose']

       if verbose:
           print(f"Przetwarzam plik {nazwa_pliku} z opcjonalną liczbą {liczba}")

       print(f"Nazwa pliku: {nazwa_pliku}")
       print(f"Liczba: {liczba}")

   if __name__ == "__main__":
       main()
   ```

   **Jak uruchomić:**

   ```shell
   python main.py example.txt --liczba=42 --verbose
   ```

### Podsumowanie

Obsługa argumentów z linii poleceń jest ważnym aspektem tworzenia programów w Pythonie. Biblioteka `argparse` jest wbudowana w standardową bibliotekę Pythona i jest wystarczająco potężna dla większości zastosowań. Alternatywy, takie jak `click` i `docopt`, oferują bardziej zwięzłe i przyjazne dla użytkownika sposoby definiowania interfejsów wiersza poleceń.

Wybór odpowiedniej biblioteki zależy od Twoich potrzeb i preferencji. `argparse` jest dobrym wyborem dla większości projektów, podczas gdy `click` i `docopt` mogą być lepsze w bardziej złożonych przypadkach lub gdy preferujesz bardziej deklaratywny styl programowania.

Jeśli masz pytania lub potrzebujesz dodatkowych wyjaśnień dotyczących konkretnej biblioteki, nie wahaj się pytać!

## Wczytywanie i parsowanie plików tekstowych

### wyrażenia regularne

### pokonywanie problemów z polskimi literami.

### Wczytywanie i parsowanie plików tekstowych w Pythonie

W Pythonie wczytywanie i parsowanie plików tekstowych jest prostym zadaniem dzięki wbudowanym funkcjom i różnym bibliotekom. W tym artykule omówimy podstawowe techniki wczytywania plików tekstowych, korzystania z wyrażeń regularnych do ich parsowania oraz radzenia sobie z polskimi literami.

#### Podstawowe wczytywanie plików tekstowych

Python oferuje wbudowane funkcje do otwierania, czytania i zapisywania plików tekstowych. Oto podstawowy przykład:

1. **Otwarcie i czytanie pliku tekstowego:**

   ```python
   # Otwarcie pliku w trybie odczytu
   with open('example.txt', 'r', encoding='utf-8') as file:
       # Odczytanie całego pliku
       content = file.read()
       print(content)
   ```

2. **Odczytanie pliku linia po linii:**

   ```python
   with open('example.txt', 'r', encoding='utf-8') as file:
       for line in file:
           print(line.strip())
   ```

3. **Zapis do pliku:**

   ```python
   with open('output.txt', 'w', encoding='utf-8') as file:
       file.write("To jest nowa linia tekstu.\n")
   ```

#### Wyrażenia regularne do parsowania tekstu

Wyrażenia regularne są potężnym narzędziem do wyszukiwania i manipulacji tekstem. Python oferuje bibliotekę `re` do pracy z wyrażeniami regularnymi.

1. **Podstawowy przykład wyrażenia regularnego:**

   ```python
   import re

   text = "To jest przykładowy tekst z numerem telefonu 123-456-789."

   # Definicja wzorca wyrażenia regularnego
   pattern = r'\d{3}-\d{3}-\d{3}'

   # Wyszukiwanie wzorca w tekście
   match = re.search(pattern, text)
   if match:
       print(f"Znaleziony numer telefonu: {match.group()}")
   ```

2. **Parsowanie pliku z użyciem wyrażeń regularnych:**

   Załóżmy, że mamy plik `data.txt` zawierający różne informacje oddzielone przecinkami, np.:

   ```
   Jan, Kowalski, 30, Warszawa
   Anna, Nowak, 25, Kraków
   ```

   Możemy użyć wyrażeń regularnych do wczytania i przetworzenia tych danych:

   ```python
   import re

   pattern = r'(\w+), (\w+), (\d+), (\w+)'

   with open('data.txt', 'r', encoding='utf-8') as file:
       for line in file:
           match = re.match(pattern, line.strip())
           if match:
               imie, nazwisko, wiek, miasto = match.groups()
               print(f"Imię: {imie}, Nazwisko: {nazwisko}, Wiek: {wiek}, Miasto: {miasto}")
   ```

#### Radzenie sobie z polskimi literami

Aby poprawnie obsługiwać polskie litery, upewnij się, że plik jest wczytywany z odpowiednim kodowaniem (np. `utf-8`).

1. **Wczytywanie pliku z polskimi literami:**

   ```python
   with open('polski_tekst.txt', 'r', encoding='utf-8') as file:
       content = file.read()
       print(content)
   ```

2. **Wyrażenia regularne z polskimi literami:**

   Jeśli potrzebujesz dopasować polskie litery w wyrażeniu regularnym, możesz użyć poniższego wzorca:

   ```python
   import re

   text = "Zażółć gęślą jaźń."

   # Definicja wzorca wyrażenia regularnego obejmującego polskie litery
   pattern = r'[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ]+'

   matches = re.findall(pattern, text)
   print(matches)
   ```

### Podsumowanie

Wczytywanie i parsowanie plików tekstowych w Pythonie jest proste dzięki wbudowanym funkcjom oraz bibliotece `re` do pracy z wyrażeniami regularnymi. Używając odpowiednich kodowań, można łatwo radzić sobie z polskimi literami. Te techniki są przydatne do przetwarzania i analizowania danych tekstowych w różnych formatach.

Jeśli masz dodatkowe pytania dotyczące wczytywania lub parsowania plików tekstowych, czy też potrzebujesz pomocy z bardziej zaawansowanymi technikami, śmiało pytaj!


### System plików w Pythonie

W Pythonie zarządzanie systemem plików jest łatwe dzięki wbudowanej bibliotece `os` oraz `os.path`. Istnieją również nowoczesne biblioteki takie jak `pathlib`, które oferują bardziej intuicyjne interfejsy. W tym artykule omówimy, jak przeglądać katalogi oraz pracować z plikami, używając zarówno tradycyjnych, jak i nowoczesnych podejść.

#### Przeglądanie katalogów

1. **Przeglądanie katalogów za pomocą `os` i `os.path`:**

   - **Listowanie zawartości katalogu:**

     ```python
     import os

     directory = '/ścieżka/do/katalogu'

     # Listowanie zawartości katalogu
     for item in os.listdir(directory):
         print(item)
     ```

   - **Rekurencyjne przeglądanie katalogów:**

     ```python
     import os

     directory = '/ścieżka/do/katalogu'

     # Przeglądanie rekurencyjne
     for root, dirs, files in os.walk(directory):
         print(f'Katalog: {root}')
         for file in files:
             print(f'  Plik: {file}')
         for dir in dirs:
             print(f'  Podkatalog: {dir}')
     ```

2. **Przeglądanie katalogów za pomocą `pathlib`:**

   `pathlib` oferuje bardziej nowoczesne podejście do pracy z systemem plików.

   - **Listowanie zawartości katalogu:**

     ```python
     from pathlib import Path

     directory = Path('/ścieżka/do/katalogu')

     # Listowanie zawartości katalogu
     for item in directory.iterdir():
         print(item)
     ```

   - **Rekurencyjne przeglądanie katalogów:**

     ```python
     from pathlib import Path

     directory = Path('/ścieżka/do/katalogu')

     # Przeglądanie rekurencyjne
     for item in directory.rglob('*'):
         print(item)
     ```

#### Praca z plikami

1. **Podstawowe operacje na plikach za pomocą `os` i `os.path`:**

   - **Sprawdzanie istnienia pliku:**

     ```python
     import os

     file_path = '/ścieżka/do/pliku.txt'

     if os.path.exists(file_path):
         print("Plik istnieje")
     else:
         print("Plik nie istnieje")
     ```

   - **Tworzenie i usuwanie plików:**

     ```python
     file_path = '/ścieżka/do/pliku.txt'

     # Tworzenie pliku
     with open(file_path, 'w') as file:
         file.write("To jest nowy plik.")

     # Usuwanie pliku
     os.remove(file_path)
     ```

   - **Kopiowanie i przenoszenie plików:**

     ```python
     import shutil

     src_path = '/ścieżka/do/pliku.txt'
     dst_path = '/ścieżka/do/nowego_miejsca.txt'

     # Kopiowanie pliku
     shutil.copy(src_path, dst_path)

     # Przenoszenie pliku
     shutil.move(src_path, dst_path)
     ```

2. **Praca z plikami za pomocą `pathlib`:**

   - **Sprawdzanie istnienia pliku:**

     ```python
     from pathlib import Path

     file_path = Path('/ścieżka/do/pliku.txt')

     if file_path.exists():
         print("Plik istnieje")
     else:
         print("Plik nie istnieje")
     ```

   - **Tworzenie i usuwanie plików:**

     ```python
     file_path = Path('/ścieżka/do/pliku.txt')

     # Tworzenie pliku
     file_path.write_text("To jest nowy plik.")

     # Usuwanie pliku
     file_path.unlink()
     ```

   - **Kopiowanie i przenoszenie plików:**

     ```python
     import shutil
     from pathlib import Path

     src_path = Path('/ścieżka/do/pliku.txt')
     dst_path = Path('/ścieżka/do/nowego_miejsca.txt')

     # Kopiowanie pliku
     shutil.copy(src_path, dst_path)

     # Przenoszenie pliku
     shutil.move(src_path, dst_path)
     ```

### Podsumowanie

Python oferuje różne narzędzia do pracy z systemem plików, zarówno za pomocą tradycyjnych modułów `os` i `os.path`, jak i nowoczesnej biblioteki `pathlib`. `pathlib` oferuje bardziej czytelny i intuicyjny interfejs, co sprawia, że jest preferowanym wyborem w nowych projektach.

Jeśli masz dodatkowe pytania dotyczące przeglądania katalogów lub pracy z plikami w Pythonie, czy też potrzebujesz pomocy z bardziej zaawansowanymi operacjami na systemie plików, śmiało pytaj!

## Komunikacja internetowa w Pythonie

Komunikacja internetowa jest kluczową częścią wielu nowoczesnych aplikacji. Python oferuje różne biblioteki i narzędzia, które umożliwiają łatwe wykonywanie zadań takich jak łączenie z serwerami SSH, transfer plików przez sFTP, pobieranie plików po HTTPS i parsowanie stron internetowych. Poniżej przedstawiamy podstawowe metody i przykłady dla każdego z tych zadań.

#### Łączenie z SSH

Do łączenia się z serwerami SSH w Pythonie można użyć biblioteki `paramiko`. Jest to potężna biblioteka do wykonywania zdalnych operacji na serwerach SSH.

1. **Podstawowe połączenie SSH:**

   ```python
   import paramiko

   hostname = 'example.com'
   port = 22
   username = 'user'
   password = 'password'

   client = paramiko.SSHClient()
   client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   client.connect(hostname, port, username, password)

   stdin, stdout, stderr = client.exec_command('ls -l')
   print(stdout.read().decode())

   client.close()
   ```

#### Łączenie z sFTP

`paramiko` może również być używane do transferu plików przez sFTP.

1. **Transfer pliku za pomocą sFTP:**

   ```python
   import paramiko

   hostname = 'example.com'
   port = 22
   username = 'user'
   password = 'password'

   transport = paramiko.Transport((hostname, port))
   transport.connect(username=username, password=password)

   sftp = paramiko.SFTPClient.from_transport(transport)
   sftp.put('localfile.txt', 'remotefile.txt')
   sftp.get('remotefile.txt', 'localfile.txt')

   sftp.close()
   transport.close()
   ```

#### Pobieranie plików po HTTPS

Do pobierania plików po HTTPS można użyć biblioteki `requests`, która jest bardzo prosta w użyciu.

1. **Pobieranie pliku:**

   ```python
   import requests

   url = 'https://example.com/file.txt'
   response = requests.get(url)

   with open('downloaded_file.txt', 'wb') as file:
       file.write(response.content)
   ```

#### Parsowanie stron internetowych (Webscraping)

Parsowanie stron internetowych jest możliwe dzięki bibliotekom takim jak `BeautifulSoup` i `requests`.

1. **Podstawowe parsowanie strony internetowej za pomocą `BeautifulSoup`:**

   ```python
   import requests
   from bs4 import BeautifulSoup

   url = 'https://example.com'
   response = requests.get(url)
   soup = BeautifulSoup(response.text, 'html.parser')

   # Znajdowanie wszystkich linków na stronie
   for link in soup.find_all('a'):
       print(link.get('href'))
   ```

2. **Parsowanie określonych elementów strony:**

   ```python
   url = 'https://example.com'
   response = requests.get(url)
   soup = BeautifulSoup(response.text, 'html.parser')

   # Znajdowanie wszystkich nagłówków h1
   for header in soup.find_all('h1'):
       print(header.text)
   ```

### Podsumowanie

Python oferuje potężne narzędzia do komunikacji internetowej, od łączenia się z serwerami SSH i transferu plików przez sFTP, po pobieranie plików po HTTPS i parsowanie stron internetowych. Biblioteki takie jak `paramiko`, `requests` i `BeautifulSoup` umożliwiają łatwe i efektywne wykonywanie tych zadań.

Jeśli masz dodatkowe pytania lub potrzebujesz bardziej zaawansowanych przykładów dotyczących któregokolwiek z tematów, śmiało pytaj!

## Dostęp do zdalnych usług typu REST API

W Pythonie dostęp do zdalnych usług REST API jest prosty dzięki bibliotece `requests`. Pozwala ona na wysyłanie zapytań HTTP oraz obsługę formatu JSON, co jest kluczowe w komunikacji z API. Poniżej znajdziesz podstawowe metody wysyłania zapytań HTTP oraz pracy z danymi w formacie JSON.

#### Wysyłanie zapytań HTTP

1. **Wysyłanie zapytania GET:**

   ```python
   import requests

   url = 'https://api.example.com/data'
   response = requests.get(url)

   if response.status_code == 200:
       print('Pomyślnie pobrano dane:')
       print(response.text)
   else:
       print(f'Błąd: {response.status_code}')
   ```

2. **Wysyłanie zapytania POST:**

   ```python
   import requests

   url = 'https://api.example.com/data'
   payload = {
       'name': 'Jan',
       'surname': 'Kowalski'
   }
   response = requests.post(url, json=payload)

   if response.status_code == 200:
       print('Pomyślnie wysłano dane:')
       print(response.text)
   else:
       print(f'Błąd: {response.status_code}')
   ```

3. **Wysyłanie zapytania PUT:**

   ```python
   import requests

   url = 'https://api.example.com/data/1'
   payload = {
       'name': 'Jan',
       'surname': 'Kowalski'
   }
   response = requests.put(url, json=payload)

   if response.status_code == 200:
       print('Pomyślnie zaktualizowano dane:')
       print(response.text)
   else:
       print(f'Błąd: {response.status_code}')
   ```

4. **Wysyłanie zapytania DELETE:**

   ```python
   import requests

   url = 'https://api.example.com/data/1'
   response = requests.delete(url)

   if response.status_code == 200:
       print('Pomyślnie usunięto dane')
   else:
       print(f'Błąd: {response.status_code}')
   ```

#### Obsługa formatu JSON

1. **Odczyt danych JSON z odpowiedzi:**

   ```python
   import requests

   url = 'https://api.example.com/data'
   response = requests.get(url)

   if response.status_code == 200:
       data = response.json()
       print('Pobrane dane JSON:')
       print(data)
   else:
       print(f'Błąd: {response.status_code}')
   ```

2. **Wysyłanie danych w formacie JSON:**

   ```python
   import requests

   url = 'https://api.example.com/data'
   payload = {
       'name': 'Jan',
       'surname': 'Kowalski'
   }
   response = requests.post(url, json=payload)

   if response.status_code == 200:
       print('Pomyślnie wysłano dane:')
       print(response.json())
   else:
       print(f'Błąd: {response.status_code}')
   ```

3. **Przykład pełnego zapytania z nagłówkami:**

   ```python
   import requests

   url = 'https://api.example.com/data'
   headers = {
       'Authorization': 'Bearer your_token_here',
       'Content-Type': 'application/json'
   }
   payload = {
       'name': 'Jan',
       'surname': 'Kowalski'
   }
   response = requests.post(url, json=payload, headers=headers)

   if response.status_code == 200:
       print('Pomyślnie wysłano dane:')
       print(response.json())
   else:
       print(f'Błąd: {response.status_code}')
   ```

### Podsumowanie

Biblioteka `requests` w Pythonie umożliwia łatwe i efektywne wysyłanie zapytań HTTP oraz obsługę danych w formacie JSON, co jest niezbędne do pracy z zewnętrznymi API. Dzięki prostocie i intuicyjności tej biblioteki, wykonywanie podstawowych operacji na API staje się szybkie i bezproblemowe.

Jeśli masz dodatkowe pytania dotyczące pracy z API lub potrzebujesz bardziej zaawansowanych przykładów, śmiało pytaj!

## Pobieranie danych z zewnętrznych źródeł: pliki płaskie CSV

Python oferuje kilka narzędzi do pracy z plikami CSV, które są jednym z najpopularniejszych formatów do przechowywania danych tabelarycznych. Najbardziej popularne biblioteki do pracy z plikami CSV to `csv` (wbudowana) oraz `pandas` (bardziej zaawansowana).

#### Wczytywanie plików CSV za pomocą `csv`

1. **Podstawowe wczytywanie pliku CSV:**

   ```python
   import csv

   with open('data.csv', mode='r', encoding='utf-8') as file:
       csv_reader = csv.reader(file)
       for row in csv_reader:
           print(row)
   ```

2. **Wczytywanie pliku CSV z nagłówkami:**

   ```python
   import csv

   with open('data.csv', mode='r', encoding='utf-8') as file:
       csv_reader = csv.DictReader(file)
       for row in csv_reader:
           print(row)
   ```

#### Wczytywanie plików CSV za pomocą `pandas`

Biblioteka `pandas` oferuje bardziej zaawansowane narzędzia do pracy z danymi tabelarycznymi i jest preferowana, gdy dane wymagają bardziej skomplikowanej analizy.

1. **Podstawowe wczytywanie pliku CSV:**

   ```python
   import pandas as pd

   df = pd.read_csv('data.csv')
   print(df)
   ```

2. **Wczytywanie pliku CSV z określonymi opcjami:**

   ```python
   import pandas as pd

   df = pd.read_csv('data.csv', delimiter=';', encoding='utf-8')
   print(df)
   ```

3. **Przykład analizy danych:**

   ```python
   import pandas as pd

   df = pd.read_csv('data.csv')

   # Wyświetlenie pierwszych kilku wierszy
   print(df.head())

   # Wyświetlenie statystyk opisowych
   print(df.describe())

   # Filtrowanie danych
   filtered_df = df[df['age'] > 30]
   print(filtered_df)
   ```

#### Pobieranie plików CSV z internetu

Często pliki CSV są dostępne do pobrania z internetu. Można je pobierać bezpośrednio do pamięci, a następnie wczytywać do `pandas`.

1. **Pobieranie i wczytywanie pliku CSV z internetu:**

   ```python
   import pandas as pd
   import requests
   from io import StringIO

   url = 'https://example.com/data.csv'
   response = requests.get(url)

   if response.status_code == 200:
       data = StringIO(response.text)
       df = pd.read_csv(data)
       print(df)
   else:
       print(f'Błąd: {response.status_code}')
   ```

2. **Pobieranie pliku CSV do lokalnego pliku:**

   ```python
   import requests

   url = 'https://example.com/data.csv'
   response = requests.get(url)

   if response.status_code == 200:
       with open('downloaded_data.csv', 'wb') as file:
           file.write(response.content)
   else:
       print(f'Błąd: {response.status_code}')
   ```

### Podsumowanie

Python oferuje różne narzędzia do wczytywania i analizy plików CSV, w tym wbudowaną bibliotekę `csv` oraz bardziej zaawansowaną bibliotekę `pandas`. `pandas` jest szczególnie przydatna do kompleksowej analizy danych. Możliwość pobierania plików CSV z internetu bezpośrednio do pamięci dodatkowo zwiększa elastyczność tych narzędzi.

Jeśli masz dodatkowe pytania dotyczące pracy z plikami CSV lub potrzebujesz bardziej zaawansowanych przykładów, śmiało pytaj!

## Odczyt i zapis do baz danych w Pythonie

Python oferuje wiele bibliotek do pracy z bazami danych, zarówno SQL, jak i NoSQL. Najpopularniejsze biblioteki to `sqlite3` do baz danych SQLite, `psycopg2` do PostgreSQL, `mysql-connector-python` do MySQL, oraz `SQLAlchemy` jako ogólne narzędzie ORM (Object-Relational Mapping).

#### Praca z SQLite

SQLite jest lekką, wbudowaną bazą danych, idealną do małych i średnich projektów.

1. **Podstawowe operacje na bazie danych SQLite:**

   ```python
   import sqlite3

   # Połączenie z bazą danych (utworzenie nowej jeśli nie istnieje)
   conn = sqlite3.connect('example.db')
   cursor = conn.cursor()

   # Utworzenie tabeli
   cursor.execute('''
       CREATE TABLE IF NOT EXISTS users (
           id INTEGER PRIMARY KEY,
           name TEXT,
           age INTEGER
       )
   ''')

   # Wstawienie danych
   cursor.execute('''
       INSERT INTO users (name, age) VALUES (?, ?)
   ''', ('Jan', 25))

   # Odczyt danych
   cursor.execute('SELECT * FROM users')
   rows = cursor.fetchall()
   for row in rows:
       print(row)

   # Zapisanie zmian i zamknięcie połączenia
   conn.commit()
   conn.close()
   ```

#### Praca z PostgreSQL

PostgreSQL jest zaawansowaną bazą danych SQL o otwartym kodzie źródłowym, popularną w większych projektach.

1. **Podstawowe operacje na bazie danych PostgreSQL:**

   ```python
   import psycopg2

   # Połączenie z bazą danych
   conn = psycopg2.connect(
       dbname='example_db',
       user='user',
       password='password',
       host='localhost',
       port='5432'
   )
   cursor = conn.cursor()

   # Utworzenie tabeli
   cursor.execute('''
       CREATE TABLE IF NOT EXISTS users (
           id SERIAL PRIMARY KEY,
           name VARCHAR(100),
           age INTEGER
       )
   ''')

   # Wstawienie danych
   cursor.execute('''
       INSERT INTO users (name, age) VALUES (%s, %s)
   ''', ('Jan', 25))

   # Odczyt danych
   cursor.execute('SELECT * FROM users')
   rows = cursor.fetchall()
   for row in rows:
       print(row)

   # Zapisanie zmian i zamknięcie połączenia
   conn.commit()
   conn.close()
   ```

#### Praca z MySQL

MySQL jest popularną bazą danych SQL używaną w wielu aplikacjach webowych.

1. **Podstawowe operacje na bazie danych MySQL:**

   ```python
   import mysql.connector

   # Połączenie z bazą danych
   conn = mysql.connector.connect(
       host='localhost',
       user='user',
       password='password',
       database='example_db'
   )
   cursor = conn.cursor()

   # Utworzenie tabeli
   cursor.execute('''
       CREATE TABLE IF NOT EXISTS users (
           id INT AUTO_INCREMENT PRIMARY KEY,
           name VARCHAR(100),
           age INT
       )
   ''')

   # Wstawienie danych
   cursor.execute('''
       INSERT INTO users (name, age) VALUES (%s, %s)
   ''', ('Jan', 25))

   # Odczyt danych
   cursor.execute('SELECT * FROM users')
   rows = cursor.fetchall()
   for row in rows:
       print(row)

   # Zapisanie zmian i zamknięcie połączenia
   conn.commit()
   conn.close()
   ```

#### Praca z SQLAlchemy

SQLAlchemy jest biblioteką ORM, która umożliwia pracę z bazami danych SQL w sposób bardziej obiektowy.

1. **Podstawowe operacje z SQLAlchemy:**

   ```python
   from sqlalchemy import create_engine, Column, Integer, String
   from sqlalchemy.ext.declarative import declarative_base
   from sqlalchemy.orm import sessionmaker

   # Tworzenie bazy danych SQLite (można też użyć innych baz danych)
   engine = create_engine('sqlite:///example.db')
   Base = declarative_base()

   # Definicja modelu
   class User(Base):
       __tablename__ = 'users'
       id = Column(Integer, primary_key=True)
       name = Column(String)
       age = Column(Integer)

   # Tworzenie tabeli
   Base.metadata.create_all(engine)

   # Tworzenie sesji
   Session = sessionmaker(bind=engine)
   session = Session()

   # Wstawienie danych
   new_user = User(name='Jan', age=25)
   session.add(new_user)
   session.commit()

   # Odczyt danych
   users = session.query(User).all()
   for user in users:
       print(user.id, user.name, user.age)

   # Zamknięcie sesji
   session.close()
   ```

### Podsumowanie

Python oferuje bogaty zestaw narzędzi do pracy z bazami danych, zarówno SQL, jak i NoSQL. W zależności od potrzeb projektu, można korzystać z prostych połączeń za pomocą `sqlite3`, `psycopg2` lub `mysql-connector-python`, albo używać bardziej zaawansowanych narzędzi jak SQLAlchemy, które ułatwiają zarządzanie bazami danych poprzez mapowanie obiektowo-relacyjne (ORM).

Jeśli masz dodatkowe pytania lub potrzebujesz bardziej zaawansowanych przykładów dotyczących pracy z bazami danych, śmiało pytaj!

## Instalowanie i korzystanie z dodatkowych bibliotek z PyPI

Python Package Index (PyPI) jest repozytorium, z którego można instalować tysiące dodatkowych bibliotek do Pythona, co pozwala na rozszerzenie funkcjonalności twoich projektów. Narzędzie `pip` jest standardowym menedżerem pakietów używanym do instalacji bibliotek z PyPI.

#### Instalowanie bibliotek za pomocą `pip`

1. **Instalowanie biblioteki:**

   Aby zainstalować bibliotekę, użyj polecenia `pip install` w terminalu lub wierszu poleceń.

   ```sh
   pip install requests
   ```

2. **Instalowanie określonej wersji biblioteki:**

   Możesz zainstalować określoną wersję biblioteki, dodając wersję do polecenia instalacji.

   ```sh
   pip install requests==2.25.1
   ```

3. **Instalowanie wielu bibliotek z pliku `requirements.txt`:**

   Jeżeli masz plik `requirements.txt` z listą bibliotek i ich wersji, możesz zainstalować wszystkie za jednym razem.

   ```sh
   pip install -r requirements.txt
   ```

   Przykładowy plik `requirements.txt`:

   ```
   requests==2.25.1
   pandas==1.2.3
   numpy==1.19.5
   ```

#### Korzystanie z zainstalowanych bibliotek

Po zainstalowaniu biblioteki możesz ją importować i korzystać z niej w swoim kodzie. Poniżej kilka przykładów, jak używać popularnych bibliotek.

1. **Korzystanie z biblioteki `requests` do pobierania danych z internetu:**

   ```python
   import requests

   response = requests.get('https://api.example.com/data')
   if response.status_code == 200:
       print(response.json())
   else:
       print('Błąd:', response.status_code)
   ```

2. **Korzystanie z biblioteki `pandas` do analizy danych:**

   ```python
   import pandas as pd

   # Wczytywanie danych z pliku CSV
   df = pd.read_csv('data.csv')
   print(df.head())

   # Podstawowa analiza danych
   print(df.describe())
   ```

3. **Korzystanie z biblioteki `numpy` do operacji numerycznych:**

   ```python
   import numpy as np

   # Tworzenie tablicy NumPy
   array = np.array([1, 2, 3, 4, 5])
   print(array)

   # Operacje na tablicy
   print(array * 2)
   ```

#### Zarządzanie zainstalowanymi bibliotekami

1. **Aktualizowanie biblioteki:**

   Aby zaktualizować bibliotekę do najnowszej wersji, użyj polecenia `pip install --upgrade`.

   ```sh
   pip install --upgrade requests
   ```

2. **Usuwanie zainstalowanej biblioteki:**

   Aby usunąć bibliotekę, użyj polecenia `pip uninstall`.

   ```sh
   pip uninstall requests
   ```

3. **Sprawdzanie zainstalowanych bibliotek:**

   Aby zobaczyć listę wszystkich zainstalowanych bibliotek, użyj polecenia `pip list`.

   ```sh
   pip list
   ```

### Podsumowanie

Instalowanie i korzystanie z dodatkowych bibliotek z PyPI za pomocą `pip` jest prostym sposobem na rozszerzenie funkcjonalności twoich projektów Pythonowych. Niezależnie od tego, czy potrzebujesz narzędzi do analizy danych, przetwarzania obrazów, komunikacji internetowej czy innych zaawansowanych funkcji, PyPI ma do zaoferowania bogaty ekosystem bibliotek, które mogą znacząco ułatwić twoją pracę.

Jeśli masz dodatkowe pytania dotyczące instalacji bibliotek lub potrzebujesz bardziej szczegółowych przykładów, śmiało pytaj!
