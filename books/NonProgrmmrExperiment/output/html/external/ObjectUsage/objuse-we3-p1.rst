ObjUse-WE3-P1
------------------

.. qnum::
   :prefix: Q
   :start: 9

    
.. topic:: Subgoals for using objects (creating instances)

   1. Declare variable of appropriate class datatype.

   2. Assign to variable: keyword new, followed by class name, followed by ().

   3. Determine whether parameter(s) are appropriate (API)

      a. Number of parameters

      b. Data types of the parameters

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: ObjUse-WE3-P1

   .. figure:: Figures/Create-instance-widget.png
      :alt: API docs for Widget constructor

   .. fillintheblank:: fill-ObjUse-WE3-P1-9

      Given this code, how many items are in mine?
      
      Widget mine = new Widget();		

      - :0: Correct
        :x: Incorrect

   .. fillintheblank:: fill-ObjUse-WE3-P1-10

      Given this code, how many items are in yours?
      
      Widget yours = new Widget(7);		

      - :7: Correct
        :x: Incorrect        

.. activecode:: ac-objuse-we3-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }