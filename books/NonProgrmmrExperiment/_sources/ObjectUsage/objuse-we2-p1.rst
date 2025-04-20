ObjUse-WE2-P1
------------------

.. qnum::
   :prefix: Q
   :start: 5

    
.. topic:: Subgoals for using objects (creating instances)

   1. Declare variable of appropriate class datatype.

   2. Assign to variable: keyword new, followed by class name, followed by ().

   3. Determine whether parameter(s) are appropriate (API)

      a. Number of parameters

      b. Data types of the parameters

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: ObjUse-WE2-P1

   .. clickablearea:: ca-ObjUse-WE2-P1-5
      :question: CClick on the variables (object references) in the following code
      :iscode:

      :click-incorrect:/* creates new random object with default seed */:endclick:
      :click-incorrect:Random:endclick: :click-correct:rand:endclick: = :click-incorrect:new Random();:endclick:
      :click-incorrect:/* creates new random object with seed parameter */:endclick:
      :click-incorrect:Random:endclick: :click-correct:rand2:endclick: = :click-incorrect:new Random(1234567890);:endclick:
      
      
   .. clickablearea:: ca-ObjUse-WE2-P1-6
      :question: Click on the class names (but not constructors) in the following code
      :iscode:

      :click-incorrect:/* creates new random object with default seed */:endclick:
      :click-correct:Random:endclick: :click-incorrect:rand:endclick: = :click-incorrect:new Random();:endclick:
      :click-incorrect:/* creates new random object with seed parameter */:endclick:
      :click-correct:Random:endclick: :click-incorrect:rand2:endclick: = :click-incorrect:new Random(1234567890);:endclick:
      
      
   .. clickablearea:: ca-ObjUse-WE2-P1-7
      :question: Click on the calls to the Random constructor in the following code
      :iscode:

      :click-incorrect:/* creates new random object with default seed */:endclick:
      :click-incorrect:Random:endclick: :click-incorrect:rand:endclick: = :click-correct:new Random();:endclick:
      :click-incorrect:/* creates new random object with seed parameter */:endclick:
      :click-incorrect:Random:endclick: :click-incorrect:rand2:endclick: = :click-correct:new Random(1234567890);:endclick:
      
      
   .. clickablearea:: ca-ObjUse-WE2-P1-8
      :question: Click on the parameters which are passed to the Random constructor in the following code
      :iscode:

      :click-incorrect:/* creates new random object with default seed */:endclick:
      :click-incorrect:Random:endclick: :click-incorrect:rand:endclick: = :click-incorrect:new Random();:endclick:
      :click-incorrect:/* creates new random object with seed parameter */:endclick:
      :click-incorrect:Random:endclick: :click-incorrect:rand2:endclick: = :click-incorrect:new Random:endclick:(:click-correct:1234567890:endclick:);
      

.. activecode:: ac-objuse-we2-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }