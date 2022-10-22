# MASTER_THESIS_NLP_enabled_synonym_detection

In the following the structure and contents of this repository are outlined.

1. 01_Code: Includes all Jupyter Notebooks with the code that is relevant for the thesis; 
          each Notebook starts with a short introduction with the purpose of the code
    
2. 02_Data: Includes all the data used within the thesis OR created during the thesis
-         - 01_labels_original: These are the original activity labels retrieved from the TU Eindhoven
          - 02_labels_adjusted: These are the adjusted labels; the adjustments mainly refer to replacements of abbreviations (see thesis section 5.1); 
                               these labels are used for further processing
          - 03_labels_augmented: This file contains all augmented labels with the WordNet enginge. We retrieved 10 synonyms for each of the       
                               02_labels_adjusted   
          - all_aug_pairs_scored_source: This is the final training data set used for fine-tuning the bi-encoder. It contains the activity label pairs and 
                                        the respective score indicating the semantical similarity.  
          - InternationalDeclarations_manipulated: Manipulated event log for evaluating the applicability of the approach
          - InternationalDeclarations_repariert: Event log after implementing the recommendations of the approach
          
3. 03_Results: This folder contains four excel files with the evaluation results
          - eval_without_fine tuning: Evaluation results with out fine-tuning the model
          - model_training_regression_domain: Evaluation and training results for evaluating the generalizability of the approach across domain
          - model_training_regression: Results of fine-tuning the bi-encoder on all 14 domains
          - scores_prototype: Similarity matrix with all the scorings of the manipulated event log during evaluation of applicability
          
