def get_css() -> str:
    """
    Return CSS styles for the Streamlit app.

    Returns
    -------
    str
        A string containing CSS styles to be applied to a Streamlit app.
    """
    
    return """
        <style>
        .stApp {
            background-color: #F2E6CC !important; /* Change this hex code to your desired background color */
        }



        # img {
        #     max-width: 100% !important;
        #     max-height: 150px !important;
        #     position: absolute  !important;
        #     /* bottom: 0; */
        #     top: 0  !important;
        #     left: 0; !important;
        #     # right: 0  !important;
        #     # -webkit-transform: scaleX(-1);
        #     # transform: scaleX(-1);

        # }
        </style>
        """