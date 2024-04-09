class Politiker:
    def __init__(self, politiker_ordbok: dict) -> None:
        self.fornavn: str = politiker_ordbok["fornavn"]
        self.etternavn: str = politiker_ordbok["etternavn"]
        self.parti: str = politiker_ordbok["parti"]["navn"]
        self.fylke: str
        self.kjønn: str = "kvinne" if politiker_ordbok["kjønn"] == 1 else "mann"
        self.komiteer: list[str] = komite
        self.verdi: int = 1000
        self.ukepoeng: list[int] = []