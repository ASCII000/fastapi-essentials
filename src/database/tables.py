"""
Tables of database
"""

from datetime import datetime
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class CargoBase(SQLModel):
    """
    Base class for role
    """

    nome: Optional[str]
    ativo: Optional[bool] = True
    criado_em: Optional[datetime] = None


class Cargo(CargoBase, table=True):
    """
    Roles with permissions
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    permissoes: List["CargoPermissao"] = Relationship(back_populates="cargo")


class PermissaoBase(SQLModel):
    """
    Base permissions of role
    """

    nome: str
    ativo: bool = True
    criado_em: datetime = Field(default_factory=datetime.utcnow)


class Permissao(PermissaoBase, table=True):
    """
    Permissions of role
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    cargos: List["CargoPermissao"] = Relationship(back_populates="permissao")


class CargoPermissao(SQLModel, table=True):
    """
    Role permissions
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    cargo_id: int = Field(foreign_key="cargo.id")
    permissao_id: int = Field(foreign_key="permissao.id")
    cargo: Optional[Cargo] = Relationship(back_populates="permissoes")
    permissao: Optional[Permissao] = Relationship(back_populates="cargos")


class ClientBase(SQLModel):
    """
    Client base
    """

    nome: str
    email: Optional[str]
    ativo: bool = True
    criado_em: Optional[datetime] = None


class Client(ClientBase, table=True):
    """
    Client table
    """
    __tablename__="clientes"
    
    id: Optional[int] = Field(default=None, primary_key=True)


class ServiceBase(SQLModel):
    """
    Service base
    """

    nome: str
    valor: float
    ativo: bool = False
    criado_em: datetime = Field(default_factory=datetime.utcnow)


class Service(ServiceBase, table=True):
    """
    Service table
    """
    __tablename__="servicos"

    id: Optional[int] = Field(default=None, primary_key=True)


class ClientService(SQLModel, table=True):
    """
    Client service table
    """
    __tablename__="clientes_servicos"

    id: Optional[int] = Field(default=None, primary_key=True)
    servico_id: int = Field(foreign_key="servico.id")
    cliente_id: int = Field(foreign_key="funcionario.id")  # conforme sua FK


class EmployeeBase(SQLModel):
    """
    Employee base
    """

    nome: Optional[str]
    email: Optional[str]
    senha: Optional[str]
    ativo: bool = False
    criado_em: Optional[datetime] = None


class Employee(EmployeeBase, table=True):
    """
    Employee table
    """
    __tablename__="funcionarios"

    id: Optional[int] = Field(default=None, primary_key=True)


class EmployeeRole(SQLModel, table=True):
    """
    Employees roles
    """
    __tablename__="funcionarios_cargos"

    id: Optional[int] = Field(default=None, primary_key=True)
    cargo_id: int = Field(foreign_key="cargo.id")
    funcionario_id: int = Field(foreign_key="funcionario.id")
