class DBRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        return model.route_tag if hasattr(model, 'route_tag') and model.route_tag else 'default'

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        return model.route_tag if hasattr(model, 'route_tag') and model.route_tag else 'default'


    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        return obj1.route_tag if hasattr(obj1, 'route_tag') and obj1.route_tag else 'default'


    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """
        return 'default'