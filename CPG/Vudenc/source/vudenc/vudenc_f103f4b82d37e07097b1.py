"""
    Root factory <=> Acl handling
"""
from pyramid.security import Allow, Deny, Everyone, Authenticated, ALL_PERMISSIONS
from sqlalchemy.orm import undefer_group
from autonomie.models.config import ConfigFiles
from autonomie.models.activity import Activity
from autonomie.models.company import Company
from autonomie.models.competence import CompetenceGrid, CompetenceGridItem, CompetenceGridSubItem
from autonomie.models.customer import Customer
from autonomie.models.files import File, Template, TemplatingHistory
from autonomie.models.project import Project, Phase
from autonomie.models.task.task import TaskLine, TaskLineGroup, DiscountLine
from autonomie.models.task.estimation import PaymentLine
from autonomie.models.task.estimation import Estimation
from autonomie.models.task.invoice import Invoice, CancelInvoice, Payment
from autonomie.models.workshop import Workshop, Timeslot
from autonomie.models.expense import ExpenseSheet, ExpensePayment, ExpenseType, ExpenseKmType, ExpenseTelType
from autonomie.models.user import User, UserDatas
from autonomie_celery.models import Job
from autonomie.models.statistics import StatisticSheet, StatisticEntry, BaseStatisticCriterion
from autonomie.models.sale_product import SaleProduct, SaleProductGroup, SaleProductCategory
from autonomie.models.tva import Tva
DEFAULT_PERM = [(Allow, 'group:admin', ALL_PERMISSIONS), (Deny,
    'group:manager', ('admin',)), (Allow, 'group:manager', ALL_PERMISSIONS),
    (Allow, 'group:contractor', ('visit',))]
DEFAULT_PERM_NEW = [(Allow, 'group:admin', ('admin', 'manage',
    'admin_treasury')), (Allow, 'group:manager', ('manage', 'admin_treasury'))]
"""
       Ressource factory, returns the appropriate resource regarding
       the request object
    """
__name__ = 'root'
@property...
"""docstring"""
acl = DEFAULT_PERM[:]
acl.append((Allow, Authenticated, 'view'))
return acl
