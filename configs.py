APIURL = 'https://demo.kitware.com/histomicstk/api/v1/'
# apiKey = None  # interactive login
apiKey = 'n0Kp1ez8YOnOiWNoACryzeBlIzbUDW3iOD2DmPLI'

source_folder_id = '5bbdeba3e629140048d017bb'

SAVEPATH = './BCSS/'
ROIBOUNDSPATH = './BCSS/meta/roiBounds.csv'

# Set either MPP or MAG.
# If both are None, base (scan) magnification is used.

# Microns-per-pixel -- best use this
# MPP of 0.25 is "standardized" at 40x using original Aperio scanners
# MPP = None
MPP = 0.25

# If you prefer to use whatever magnification is reported
MAG = None
# MAG = 40.0

# What things to download? -- comment out whet you dont want
PIPELINE = (
    'images',
    'masks',
    'annotations',
)

# if you only want to download data for specific slides
SLIDES_TO_KEEP = None
#SLIDES_TO_KEEP = ['TCGA-A1-A0SP', 'TCGA-A2-A04P', 'TCGA-A2-A04Q', 'TCGA-A2-A04T', 'TCGA-A2-A0CM']
