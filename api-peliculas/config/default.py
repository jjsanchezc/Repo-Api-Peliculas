SECRET_KEY = '123447a47f563e90fe2db0f56b1b17be62378e31b7cfd3adc776c59ca4c75e2fc512c15f69bb38307d11d5d17a41a7936789'			
PROPAGATE_EXCEPTIONS = True
# Primero se usa la ip del clusterip del servicio, se sube la imagen
# se hace el flask db init y todo eso con la ip externa
SQLALCHEMY_DATABASE_URI='postgresql://sjmbhpsc:Sx8H5Lk9V7S0mDZQEs0dz1mwubxO4nKt@35.224.43.62:5432/sjmbhpsc'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SHOW_SQLALCHEMY_LOG_MESSAGES = False
ERROR_404_HELP = False