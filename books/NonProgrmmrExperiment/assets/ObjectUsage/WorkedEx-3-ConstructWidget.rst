Worked Example: Create Instance of Widget
==============================================

.. topic:: Subgoals for using objects (creating instances)

   1. Declare variable of appropriate class datatype.
    
   2. Assign to variable: keyword new, followed by class name, followed by ().
    
   3. Determine whether parameter(s) are appropriate (API)
    
      a. Number of parameters
        
      b. Data types of the parameters
      
You can watch this video or read through the content below it.

.. youtube:: sc5zgcAIY3M
   :divid: video-useobj-we1-create-widget
   :align: center
       
.. topic:: Custom Classes

   ``Widget`` is a made-up class for this lesson. As you become proficient in Java, you will write your own classes, as well. Luckily, the developers who defined the Widget class provided the following constructor documentation.

   .. figure:: Figures/Create-instance-widget.png
      :alt: API docs for Widget constructor
        
   Unfortunately, because we do not have an implementation of the Widget class, the ActiveCode block below will not work with the Widget class. When you get to the end of this lesson, try to use the subgoals to reconstruct your work from the previous lesson on the Random object, without looking.


.. topic:: SG1: Declare variable of appropriate class datatype.
    
   .. code-block:: java
    
      Widget alpha;
      
.. topic:: SG2: Assign to variable:  keyword new, followed by class name, followed by ().
    
   .. code-block:: java
    
      alpha = new Widget();
        
.. topic:: SG3: Determine whether parameter(s) are appropriate (API)

   In the photo of the documentation above, we can specify any ``int`` value for how many items we want in the widget object.
      
   .. code-block:: java
    
      alpha = new Widget(42);
        
.. activecode:: ac-objectuse-we3
   :language: java

   public class main{
      public static void main(String args[]){   
      }
   }
      
      
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      objuse-we3-p1.rst