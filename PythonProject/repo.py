#repo é tipo o back
from pathlib import Path
import json, csv

class LeadRepository:
    def __init__(self):
        self.DATA_DIR = Path(__file__).resolve().parent / "data"#caminho da paste repo
        self.DATA_DIR.mkdir(exist_ok=True) #cria a pasta ?
        self.DB_PATH = self.DATA_DIR / "leads.json" # cria o json bd

    #retorna os dados carregados

    #----------------
    #Métodos privados
    #----------------
    def _load(self): #_ indica que só vai usar a função nesse arquivo
        if not self.DB_PATH.exists(): #se esse arquivo não existe
            return [] #retorna o array de dicionários vazio

        try:
            return json.loads(self.DB_PATH.read_text(encoding="utf-8"))#lê um texto e converte p dicionário  # utf8 -> lê todos os caracteres do nosso idioma
        except json.JSONDecodeError:
            return [] #retorna o array de dicionários vazio se tiver algum erro

    #precisa dos leads pra salvar o arquivo
    def _save(self, leads):
        self.DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8") #json.dumps lê o dicionário e converte pra texto
        #ensure_ascii -> algo com binário ?

    #API PÚBLICA, aqui você cria a rota
    def create_lead(self, lead_dict): #novo lead modelado no front
        leads_loaded = self._load() # 1° vez retorna array vazio
        leads_loaded.append(lead_dict)
        self._save(leads_loaded)

    def read_leads(self):
        return self._load()

    def export_csv(self): #cria um arquivo csv
        path_csv = self.DATA_DIR / "leads.csv"
        leads = self._load()

        try:
            with path_csv.open("w", newline = "", encoding = "utf-8") as file:
                writer = csv.DictWriter(file, fieldnames = ["name", "company", "email", "stage", "created"]) #nome dos campos

                writer.writeheader() #pega o cabeçalho e coloca no arquivo
                for lead in leads:
                    writer.writerow(lead)

            return path_csv
        except PermissionError: #Erro
            #caso o arquivo esteja aberto
            return None

