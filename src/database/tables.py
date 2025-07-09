"""
Tables of database
"""

from datetime import datetime
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class RoleBase(SQLModel):
    """
    Base class for role
    """

    nome: Optional[str]
    ativo: Optional[bool] = True
    criado_em: Optional[datetime] = None


class Role(RoleBase, table=True):
    """
    Roles with permissions
    """
    __tablename__="cargos_permissoes"

    id: Optional[int] = Field(default=None, primary_key=True)
    permissoes: List["RolePermission"] = Relationship(back_populates="cargo")


class PermissionBase(SQLModel):
    """
    Base permissions of role
    """

    nome: str
    ativo: bool = True
    criado_em: datetime = Field(default_factory=datetime.utcnow)


class Permission(PermissionBase, table=True):
    """
    Permissions of role
    """
    __tablename__="permissoes"

    id: Optional[int] = Field(default=None, primary_key=True)
    cargos: List["RolePermission"] = Relationship(back_populates="permissao")


class RolePermission(SQLModel, table=True):
    """
    Role permissions
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    cargo_id: int = Field(foreign_key="cargo.id")
    permissao_id: int = Field(foreign_key="permissao.id")
    cargo: Optional[Role] = Relationship(back_populates="permissoes")
    permissao: Optional[Permission] = Relationship(back_populates="cargos")


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
