# from stages import model_leads
from model import Lead
from stages import stage_status #1
# from stages import DEFAULT_STAGES #2
from repo import LeadRepository


lead_backend = LeadRepository()

#simula o frontend
def add_lead():
    name = input("Nome: ")
    company = input("Empresa: ")
    email = input("Email: ")
    stage_client = str(stage_status())
    lead = Lead(name, company, email, stage_client) #1

    modeled_lead = lead.model_leads() #dicionário
    lead_backend.create_lead(modeled_lead) # OBScriar um metodo pra modificar os estágios depois
    print("Lead adicionado")

def list_leads():
    leads = lead_backend.read_leads()
    # print(leads)

    if not leads:
        print("Nenhum lead ainda")
        return

    print(f"\n## | {"Nome":<20} | {"Empresa":<20} | {"Email":<20} | {"Status":<20}") #padroniza espaço
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]:<20} | {lead["company"]:<20} | {lead["email"]:<20} | {lead["stage"]:<20}") #i:02d é duas casas decimais

def search_leads():
    user_search = input("Buscar por: ").strip().lower() #.strip tira os espaços do início e fim
    if not user_search:
        print("Consulta vazia")
        return

    leads = lead_backend.read_leads()
    results = []

    for i, lead in enumerate(leads):
        lead_str = f"{lead["name"]} {lead["company"]} {lead["email"]} {lead["stage"]}".lower()
        if user_search in lead_str:
            results.append(lead)

    if not results:
        print("Nada encontrado!")
        return

    print(f"\n## | {"Nome":<20} | {"Empresa":<20} | {"Email":<20} | {"Status":<20}")  # padroniza espaço
    for i, lead in enumerate(results):
        print(f"{i:02d} | {lead["name"]:<20} | {lead["company"]:<20} | {lead["email"]:<20} | {lead["stage"]:<20}")  # i:02d é duas casas decimais

def export_leads():
    path_csv = lead_backend.export_csv()
    if path_csv is None:
        print("Não foi possível exporar os leads como CSV")
    else:
        print(f"Leads exportados como CSV para: {path_csv}")


def main():
    while True:
        print_menu()
        op = input("Escolha: ")

        if op == "1":
            add_lead()
        elif op == "2":
            list_leads()
        elif op == "3":
            search_leads()
        elif op == "4":
            export_leads()
        elif op == "0":
            print("Até mais")
            break
        else:
            print("Opção inválida")

def print_menu():
    print("\nMini CRM de Leads - (Adicionar/listar)")
    print("[1] Adicionar Lead")
    print("[2] Listar Leads")
    print("[3] Buscar lead por (nome/empresa/email):")
    print("[4] Exportar leads como CSV")
    print("[0] Sair do programa")

# main()
if __name__ == "__main__":
    main()