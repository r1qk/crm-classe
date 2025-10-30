from datetime import date

class Lead:
    def __init__(self, name, company, email, stage):
        self.name = name
        self.company = company
        self.email = email
        self.stage = stage
        self.created = date.today().isoformat()  # -> isoformat tira o datetime quando exibir no print


    def model_leads(self):  # criar/modelar um lead como um dicionário simples
        return {
            "name": self.name,
            "company": self.company,
            "email": self.email,
            "stage": self.stage,
            "created": self.created
        }

# STAGES = ["novo"]  # por enquanto, só marcamos como novo


