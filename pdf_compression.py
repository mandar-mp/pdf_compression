# %% [markdown]
# # PDF compression
# ## This code reduces pdf file size by compressing images from the pdf
# ## Install below python libraries
# ### pip install pypdf
# ### pip install pypdf[image]

# %%
from pypdf import PdfWriter

# %%
# source file path
input_file = ""
#destination file path
output_file = ""

writer = PdfWriter(clone_from==input_file)

for page in writer.pages:
    for image in page.images:
        image.replace(image.image,quality=30)


with open(output_file,"wb") as f:
    writer.write(f)

print("Pdf file compressed successfully!")


