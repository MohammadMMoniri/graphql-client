from typing import List, Dict
import json
from keyword import iskeyword


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

        for field in fields:
            if (not isinstance(field, str) or not field.isidentifier() or iskeyword(field)):
                raise Exception(f'you cant use "{field}" as field name.')
            self.__setattr__(field, None)
        print(json.dumps(query))


class Query:
    linked_list = []

    def __init__(self, entity, fields, query) -> None:
        self.master_entity = Entity(
            entity_name=entity, fields=fields, father=None
        )
        pass

    def add_to_felids(self):
        pass
