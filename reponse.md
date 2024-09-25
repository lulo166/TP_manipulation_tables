P1
Ex1: les tables ville et evolution
Ex2/3: la table ville a les attributs code, region, departement, nom, et coordonnees, avec code comme cle primaire, il n'y a pas de cle etrangeres.
       la table evolution a les attributs code, categories, genre et effectif, et n'a pas de cle primaires, mais a une cle etrangere appele code, qui est lie a la table ville.
Ex4: j'utilise les contraintes d'integrite referentielles avec 'PRAGMA foreign_keys = ON;'
Ex5: Fait

P2
Ex1: SELECT * FROM evolution;
Ex2: SELECT categorie FROM evolution;
Ex3: SELECT DISTINCT categorie FROM evolution;
Ex4: SELECT nom, code FROM ville WHERE code = '59350'; le nom de la ville est lille.
Ex5: SELECT code FROM ville WHERE nom = 'Caullery'; le code est 59140.
Ex6: SELECT * FROM evolution WHERE code = '59350';
Ex7: SELECT * FROM evolution WHERE code = '59350' ORDER BY effectif DESC;
Ex8: SELECT code FROM evolution WHERE effectif > 2000;
Ex9: SELECT DISTINCT ville.nom FROM ville INNER JOIN evolution ON ville.code = evolution.code WHERE evolution.effectif > 2000;
Le resultat est Maubeuge, Tourcoing, Dunkerque, Marcq-en-Baroeul, Halluin, Roubaix, Wattrelos, Coudekerque-Branche, Douai, Lambersart, Valenciennes, Lille               
Grande-Synthe       
Bailleul            
Sin-le-Noble        
Cambrai             
Ronchin             
Faches-Thumesnil    
Loos                
Mons-en-Baroeul     
Croix               
Villeneuve-d'Ascq   
La Madeleine        
Denain              
Hazebrouck          
Armentières         
Wasquehal           
Hem                 
Saint-Amand-les-Eaux