from workflows.comic_workflow import ComicWorkflow

workflow = ComicWorkflow()

comic = workflow.run(

"""
A boy learns cycling.

He falls.

His father teaches him.

He wins.
"""

)

comic.save("outputs/final_comic_gemini.png")