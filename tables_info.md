cid  name         type  notnull  dflt_value  pk
---  -----------  ----  -------  ----------  --
0    code         TEXT  0                    1 
1    region       TEXT  0                    0 
2    departement  TEXT  0                    0 
3    nom          TEXT  0                    0 
4    coordonnees  TEXT  0                    0 
sqlite> PRAGMA table_info(evolution);
cid  name       type     notnull  dflt_value  pk
---  ---------  -------  -------  ----------  --
0    code       TEXT     0                    0 
1    categorie  TEXT     0                    0 
2    genre      TEXT     0                    0 
3    effectif   INTEGER  0                    0 