from typing import List, Dict
import json


class Entity:
    def __init__(self, entity_name: str, fields: List[str], query: Dict, father) -> None:
        if father == None:
            self.is_master = True
        else:
            self.is_master = False
        self.entity_name = entity_name
        self.fields = fields
        self.query = query
        self.father = father

        for i in fields:
            if (type(i) != str):
                raise Exception('you are a whore.')
            self.__setattr__(i, None)
        print(json.dumps(query))


kir = Entity('kir', ['id', 'nam'], {"salam": None}, None)


class Query:
    linked_list = []

    def __init__(self, entity, fields, query) -> None:
        self.master_entity = Entity(
            entity_name=entity, fields=fields, father=None
        )
        pass

    def add_to_felids(self):
        pass
