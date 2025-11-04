create table clients (code_client varchar(8) primary key not null,  nom_client varchar(50), prenom_client varchar(50), ville_client varchar(50), email_client varchar(50), type_client varchar(50));

create table fournisseurs (code_fournisseur varchar(8) primary key not null, nom_fournisseur varchar(50));

create table articles (code_client varchar(8) primary key not null,  libelle_article varchar(50), poids_article varchar(50), couleur_article varchar(50), prix_vente varchar(50), prix_achat varchar(50), stock varchar(50), article_fournisseur varchar(8), code_categorie varchar(8));

create table categories (code_categorie varchar(8) primary key not null, libelle_categorie varchar(50));

create table commandes (code_commande varchar(8) primary key not null, code_client varchar(8), foreign key (code_client) references clients(code_client));

create table lig_cmd(code_commande varchar(8), code_article varchar(8), quantite varchar(50), foreign key (code_article) references articles(code_article), foreign key (code_commande) references commandes(code_commande));

create table livreur (id_livreur varchar(8) primary key not null, raison_social varchar(100));


create table colis( code_colis varchar(8) primary key not null, date_livraison date, code_livreur varchar(8), code_commande varchar(8), foreign key (code_livreur) references livreur(id_livreur), foreign key (code_commande) references commandes(code_commande));

alter table clients modify ville_client default 'Berkane'; success
alter table clients modify adresse_client varchar(255); success

alter table articles add foreign key (article_fournisseur) references categories(code_categorie)

alter table articles add foreign key (code_categorie) references categories(code_categorie)
alter table articles add foreign key (article_fournisseur) references fournisseurs(code_fournisseur);

alter table articles rename column code_client to code_article; succcess
alter table lig_cmd rename to details_commande; success

alter table articles modify (prix_vente float, prix_achat float, stock float); success


alter table articles add constraint pos_val_ck check( prix_vente > 0 and prix_achat > 0 and stock > 0); success
 
alter table clients add check( type_client in ('particulier', 'administration', 'grand compte', 'pme')); success

alter table clients modify ville_client not null; success

alter table commandes drop primary key cascade; success

select constraint_name, constraint_type from user_constraints where table_name = 'COMMANDES';
alter table commandes disable constraint SYS_C008329; success

SELECT constraint_name, constraint_type,
search_condition
FROM
user_constraints
WHERE table_name = 'COMMANDES' 👀;

exo2
create table etudiants(num_etudiant int primary key, nom varchar(50), prenom varchar(50));
create table matieres(code_mat int primary key, libelle_mat varchar(50), coeff_mat varchar(50));
create table evaluations (num_etudiant int, code_mat int, date_jour date, note float);
alter table evaluations add foreign key (num_etudiant) references etudiants(num_etudiant);alter table evaluations add foreign key (code_mat) references matieres(code_mat);
alter table evaluations add primary key (num_etudiant, code_mat);

alter table matieres modify libelle_mat unique; success

alter table matieres add check(coeff_mat > 0);
