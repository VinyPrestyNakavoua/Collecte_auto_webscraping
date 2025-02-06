# Collecte_auto_webscraping
## Webscraping : Qu’est-ce que c’est ?
Le webscraping désigne les techniques d’extraction du contenu des sites internet. C’est une pratique très utile
pour toute personne souhaitant travailler sur des informations disponibles en ligne, mais pas nécessairement
accessible par une API.
L’idée générale va être de charger le code source de la page web puis d’aller chercher dans celui-ci les informations
souhaitées.

Commençons par un rappel rapide de la structure d’un site web : Un site Web est un ensemble de pages
codées en HTML qui permet de décrire à la fois le contenu et la forme d’une page Web.

Sur une page web, vous trouverez toujours à coup sûr des éléments comme <head>, <title>, etc. Il s’agit des
codes qui vous permettent de structurer le contenu d’une page HTML et qui s’appellent des balises. Citons,
par exemple, les balises <p>, <h1>, <h2>, <h3>, <strong> ou <em>. Le symbole < > est une balise :
il sert à indiquer le début d’une partie. Le symbole </ > indique la fin de cette partie. La plupart des balises
vont par paires, avec une balise ouvrante et une balise fermante (par exemple <p> et </p>).

Pour récupérer correctement les informations d’un site internet, il faut pouvoir comprendre sa structure et
donc son code HTML. Les fonctions python qui servent au scraping sont principalement construites pour vous
permettre de naviguer entre les balises.

## Webscraping en python
De manière assez similaire à l’utilisation d’API, faire du webscrapping en python commence par faire la requête
de la page web.

La différence principale est qu’à ce moment-la, plutôt que de récupérer des données pré-formatées dans un
format json, xml ou csv, on récupère le code brut de la page web, qu’il va falloir explorer pour obtenir les
données voulues.

Pour cela, on va se servir de la bibliothèque BeautifulSoup. (D’autres existent, notamment Selenium, qui vous
permettra de faire du webscrapping sur les parties dynamiques des pages, sur lequel on reviendra plus bas).
Son rôle va être de structurer la donnée récupérée afin d’accéder facilement à son contenu en filtrant sur les



## Les Bonnes Pratiques de Webscraping [Cours]
Le webscraping est une activité qui peut causer un certain nombre de problèmes aux sites ciblés, ce qui en
fait quelque chose d’assez mal vu en général. Pour faire du webscraping de manière polie et raisonnable, il y
a quelques règles à suivre :
— Comme pour les API, assurez-vous de limiter vos chargements de pages au strict nécessaire.
— Insérez des pauses entre les différents appels pour ne pas surcharger les serveurs ( En python, vous
pourrez utilisez la méthode sleep de la bibliothèque time.
— Souvenez-vous qu’il est illégal de webscraper des données considérées comme personnelles, même si
elles sont publiées sur un site.
— Respectez les souhaits des webmaster du site concernant ce qui est, ou non, webscrapable sur le site
en question.

Pour ce dernier point, vous pourrez par exemple vérifier ce qui est indiqué sur le robots.txt du site web.

robots.txt est un fichier disponible normalement sur tout site web (à l’adresse http ://www.adressedusite.com/robots.txt)
et indiquant ce qu’il est possible de faire sur le site. Initialement créé pour les robots de moteur de recherche,
il est aussi utilisé pour indiquer les limites du webscraping.


## Webscraper des pages dynamiques [Cours]
Nous avons précédemment vu comment récupérer les données de pages statiques ( où l’ensemble des données
est présent dans le code html de la page à étudier). Nous allons maintenant voir comment récupérer les
données pages dynamiques, contenant notamment du javascript. Nous allons pour cela utiliser la bibliothèque
Selenium de python.

Cette bibliothèque permet de simuler une connection depuis un navigateur web, et de manipuler la page
comme pourrait le faire un utilisateur. En particulier, il est possible pour le programme python de scroller
pour charger plus de la page, de cliquer sur des boutons, ou de remplir des formulaires, notamment d’authentification.
Vous aurez besoin d’installer la bibliothèque selenium, mais aussi la bibliothèque webdriver_manager pour
simplifier les choses.



balises par exemple.
