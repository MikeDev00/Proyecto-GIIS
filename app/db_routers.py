from home.models import PruebaBit, Usuario

class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model is Usuario:
            return "users"
        return None

    def db_for_write(self, model, **hints):
        if model is Usuario:
            return "users"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.model == Usuario and  obj2._meta.model == PruebaBit:
            return True
        return None

    def allow_migrate(self, db,app_label, model_name=None, **hints):
        if model_name == Usuario.__name__.lower():
            return db == "users"
        else: 
            return db == "default"
       



