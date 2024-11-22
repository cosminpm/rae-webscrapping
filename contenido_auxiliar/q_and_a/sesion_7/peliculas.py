def fetch_pelicula(name: str) -> str:
    with UnitOfWork() as uow:
        orm = uow.session.query(...).filter_by(name=name).first()
        return orm.id
# id - name ha sido manualmente antes aniadido
# name -> bd -> id -> web -> infor