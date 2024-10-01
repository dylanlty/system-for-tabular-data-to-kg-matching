'''
A System for Tabular data to Knowledge Graph Matching

Created in 2024
@author: dylanlty
'''

from lookup import DBpediaLookup, WikidataAPI


Config = {
    "dbpedia": {
        "KG_api": DBpediaLookup(),
        "KG_source": "DBpedia",
        "KG_link_template": "http://dbpedia.org/resource/#####",
    },                 
    "wikidata": {
        "KG_api": WikidataAPI(),
        "KG_source": "Wikidata",
        "KG_link_template": "http://www.wikidata.org/entity/#####",     
    },
}