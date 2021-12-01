# Mitosis classification with CNN and explainable model 

![Untitled](https://user-images.githubusercontent.com/29009898/138671190-4f1a751b-9a79-48c0-8e2f-e4a402c280b4.gif)
> This image shows a dividing CHO (Chinese Hamster Ovary) Cell. The predicted cell state is labelled on the top left via the CNN model. Further, the trained CNN model is investigated with the LIME algorithm for explainability. The red patch shows the region that causes a negative score for this classification and the green patch shows the positive one. 

## What is this project about?

This project used convolutional neural network to classify mitotic stages via microscopic imaging. Noted that the classification is based on either nucleus or mitochondrial morphology to obtain time series classification. After CNN was trained, we applied LIME and SHAP algorithm to investigate the attention of the trained neural network. This is a pipeline to implement reliable classification algorithm with cell images.

## Why automatic classification of mitotic stages is useful?

Most of cancer cells possess abnormal division process, and cell division state is a critical feature for pathological diagnosis. However, there is limited stained and fluorescent method to visualize the internal structure of a cell. Thus, indirect morphology changes is sometimes the only hint to understand the mitotic stage of the cell. In this research, we used mitochondrial morphology to classify the nucleus-related event, and shows that CNN is able to tackle with hidden mitotic information. 

Possible application includes clinical diagnosis of imaging data that comes from high-throughout device like High Content, and tissue sections. Our aim is to provide automatic mitotic segmentation to understand the population status of the target tissue.  Finally, we applied SHAP and LIME to provide the explainability of the trained CNN model.

## Presentation

[![](https://user-images.githubusercontent.com/29009898/138673697-f7ada74a-9c14-4799-be4f-1195bbdbdbfd.png)](https://docs.google.com/presentation/d/1ehAQE3JU7z6V9cX56RJXGWztyd_5NdBW/edit?rtpof=true&sd=true)
> [Link](https://docs.google.com/presentation/d/1ehAQE3JU7z6V9cX56RJXGWztyd_5NdBW/edit?usp=sharing&ouid=115922715586840460448&rtpof=true&sd=true)

## Authors

- [stevengogogo](https://github.com/stevengogogo)
- [VillaHsu](https://github.com/VillaHsu)
