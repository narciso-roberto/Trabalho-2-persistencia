from dtos.createTransacaoDTO import CreateTransacaoDTO
from datetime import datetime

class UpdateTransacaoDTO(CreateTransacaoDTO):
    data_transacao: datetime | None = None