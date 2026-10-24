# sqlite-affinity-probe

## Français

Révéler les résultats changés par les affinités de types SQLite.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m sqlite_affinity_probe examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Crée une vraie base SQLite en mémoire pour chaque affinité, insère les mêmes scalaires liés et observe stockage et lignes retenues. Le résultat distingue la sémantique native de la formulation générée par un LLM.

### Limites

Une colonne, prédicats bornés et affinités SQLite non STRICT ; pas une preuve déquivalence SQL générale ni une simulation MySQL/PostgreSQL.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Expose results changed by SQLite type affinities.

Synthetic data; no network access or secret required.

```sh
python -m sqlite_affinity_probe examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Creates a real in-memory SQLite database per affinity, binds the same scalars and observes storage and matched rows. Separates native semantics from an LLM-generated formulation.

### Limits

One column, bounded predicates and non-STRICT SQLite affinities; no general SQL-equivalence proof or MySQL/PostgreSQL simulation.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Revelar resultados alterados por afinidades de tipos SQLite.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m sqlite_affinity_probe examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Crea una base SQLite real en memoria por afinidad, vincula los mismos escalares y observa almacenamiento y filas seleccionadas. Separa semántica nativa de una formulación generada por un LLM.

### Límites

Una columna, predicados acotados y afinidades SQLite no STRICT; sin prueba general de equivalencia SQL ni simulación MySQL/PostgreSQL.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.sqlite.org/datatype3.html
