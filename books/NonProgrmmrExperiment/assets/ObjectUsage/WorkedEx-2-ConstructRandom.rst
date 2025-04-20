Worked Example: Create Instance of Random
==============================================

.. topic:: Subgoals for using objects (creating instances)

   1. Declare variable of appropriate class datatype.
    
   2. Assign to variable: keyword new, followed by class name, followed by ().
    
   3. Determine whether parameter(s) are appropriate (API)
    
      a. Number of parameters
        
      b. Data types of the parameters
       
You can watch this video or read through the content below it.

.. youtube:: JK3qGCUhq3o
   :divid: video-useobj-we1-create-random
   :align: center   
   
.. topic:: SG1: Declare variable of appropriate class datatype.

   In the code block below, the variable name ``randGen`` was selected to better describe this object's purpose as a random number generator.
    
   .. code-block:: java
    
      Random randGen;
      
.. topic:: SG2: Assign to variable:  keyword new, followed by class name, followed by ().
    
   .. code-block:: java
    
      randGen = new Random();
        
.. topic:: SG3: Determine whether parameter(s) are appropriate (API)

   The figure below shows the Java documentation, so we can determine what parameter(s) we need. If we wanted a specific seed value, we could use that, but for most purposes, allowing the constructor to select its own seed is ok.

   .. figure:: Figures/Create-instance-random.png
      :alt: API docs for Random constructor
        
.. activecode:: ac-objectuse-we2
   :language: java

   import java.util.Random;
   public class main{
      public static void main(String args[]){   
      }
   }
      
      
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      objuse-we2-p1.rst