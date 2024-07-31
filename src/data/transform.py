from src.utils import get_nl, insert_substring_before_encoding
from src.vegazero.vegazero import VegaZero2VegaLite


def extract_response(stream:str) -> str:
    """
    Extract and format the response from a stream of text.

    Parameters
    ----------
    stream : str
        The stream of text containing the response data.

    Returns
    -------
    str
        The formatted response extracted from the stream.
    """
    response = get_nl(stream, pattern=r"## Response:(.+)")
    response = response.replace("Step 3.", "\n Step 3.")
    response = response.replace("Step 2.", "\n Step 2.")
    response = response.replace("  ", "")
    response = response.split('Step 2. Visualization explanation:')[1]
    response = "*(Explanation)*" + response

    try:
        response = response.replace("The visualization is ", "\n *(Caption)* The visualization is ")
    except:
        try:
            response = response.replace("The visualization represents", "\n *(Caption)* The visualization represents ")
        except:
            try:
                response = response.replace("This is a ", "\n *(Caption)* This is a ")
            except:
                pass
    
    response = response.replace('Step 3. Insights suggestions:', '\n *(Suggest)* Other instructions to generate other data visualizations, based on the generated one, could include:\n')
    return response

def extract_visualization(stream:str) -> str:
    """
    Extract and transform a VegaZero visualization description from a stream of text into a VegaLite format.

    Parameters
    ----------
    stream : str
        The stream of text containing the VegaZero visualization data.

    Returns
    -------
    str
        The transformed VegaLite visualization description.
    """
    vz = VegaZero2VegaLite()
    pred_vis_ = get_nl(stream, pattern=r"Step 1\. Vegazero visualization:(.+?)Step 2\.").strip()
    pred_vis = insert_substring_before_encoding(pred_vis_, " data dataset ")
    pred_vis = pred_vis.replace(",", '')
    pred_vis_vl,_ = vz.to_VegaLite(pred_vis)
    return pred_vis_vl

def build_prompt(query: str, dataset: str) -> str:
    """
    Build a prompt for recommending and explaining the best visualization for a dataset.

    Parameters
    ----------
    query : str
        The query or request from the user for visualization.
    dataset : str
        The dataset description to be visualized.

    Returns
    -------
    str
        A formatted prompt string containing the query, dataset, and instructions for visualization recommendation.
    """
    
    return f""" 
    Your task is to recommend and explain to a user the best visualization for a given dataset using the VegaZero template. 
    Here are the available options: mark [T], encoding x [X], y [Y], aggregate [AggFunction], color [Z], transform filter [F], group [G], bin [B], sort [S], topk [K]. 
    
    Let's think step by step.
    ## Request: 
    {query}                                                                                                                                                 
    ## Dataset: 
    {dataset}
    ## Reasoning process:
    """

