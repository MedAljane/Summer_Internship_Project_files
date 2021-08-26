# WebScrapping internship files

## Description
  
  Repository to store the files produced during the WebScrapping internship and their versions
 
 ## Prerequisites
   - **Python3.8 at least**
   - deep-translator (GoogleTranslator included here)
   - selenium
   - bs4 (BeautifulSoup)
   - re (RegEx)
   - pandas
   - numpy
   - seaborn
   - json
   - requests
   - urllib
   - textblob
   - **For the paraphraser**:
     - sentence-splitter
     - transformers
     - SentencePiece
     - cdifflib
     - nltk
     - torch

## Setting up the transPhraser
### For **online** usage
  - In the **pegasus_paraphrase.py** file, set the **model_name** variable's value to "tuner007/pegasus_paraphrase" (this will download the required files once the script is imported and will download at each system start)
  
### For **local** usage
  - Download the required files from this [link](https://huggingface.co/tuner007/pegasus_paraphrase/tree/main) to a folder in the working directory
  - In the **pegasus_paraphrase.py** file, set the **model_name** variable's value to the path of the folder where you downloaded the files
  
### Side note for the CUDA usage (using graphic card CUDA Cores for the script)
  - If you wish to use CUDA while running the script for higher performance:
  1. Chek if your graphic card has the CUDA Computing capability
  2. Download the required CUDA Computing Toolkit
  3. Reinstall torch (if you still get the same Torch version, try to follow the solution presented in this [comment](https://github.com/pytorch/pytorch/issues/30664#issuecomment-896303074))
  
  - If you still get the CPU as **torch_device**, copy the path of the binary files for the CUDA toolkit and paste it as parameter in the **os.add_dll_directory()** in the **pegasus_paraphrase.py** file (in my version of the code, I have my **bin** folder under "C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.4/" follow that example and replace it with your own path)

   
## Contact
   - Mohamed Amine Aljane;
     - Aljane.medamine.97@gmail.com
     - [LinkedIn Profile](https://www.linkedin.com/in/almedamine/)
