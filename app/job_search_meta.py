class JobSearchAppMeta(type):
  
    def __call__(cls, *args, **kwargs):
      
        # Создает экземпляр класса, и вызывает взаимодействие с пользователем.
      
        instance = super().__call__(*args, **kwargs)
        instance._interact_with_user()
        return instance
