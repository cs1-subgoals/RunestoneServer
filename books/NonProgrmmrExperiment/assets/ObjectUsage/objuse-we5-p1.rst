ObjUse-WE5-P1
------------------

.. qnum::
   :prefix: Q
   :start: 14

    
.. topic:: Subgoals for Calling a Method

   1. Classify method as static method or instance method
      
      a. If static, use the class name

      b. If instance, must have or create an instance 
        
   2. Write (instance / class) dot method name and ( )

   3. Determine whether parameter(s) are appropriate
      
      a. Number of parameters passed must match method declaration

      b. Data types of parameters passed must match method declaration (or be assignable)
   
   4. Determine what the method will return (if anything: data type, void, print, change state of object) and where it will be stored (nowhere, somewhere)

   5. Evaluate right hand side (RHS) of assignment (if there is one). Value is dependent on method's purpose

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: ObjUse-WE5-P1


   .. fillintheblank:: fill-ObjUse-WE5-P1-14

      What number goes in the blank so that a random value between 0 and 5 will be generated? 
      
      Random random = new Random();
      int die = random.nextInt(_______);

      - :6: Correct
        :x: Incorrect
        
        
   .. clickablearea:: ca-ObjUse-WE5-P1-15
      :question: Click on the method calls of the Random instance in the following code
      :iscode:
      
      :click-incorrect:Random:endclick: :click-incorrect:rand:endclick: = :click-incorrect:new Random():endclick:;
      :click-incorrect:int:endclick: :click-incorrect:flippedCoin:endclick: = :click-incorrect:rand:endclick::click-correct:.nextInt(2):endclick:;
      :click-incorrect:int:endclick: :click-incorrect:playingCard:endclick: = :click-incorrect:rand:endclick::click-correct:.nextInt(52):endclick:;
      
      
   .. clickablearea:: ca-ObjUse-WE5-P1-16
      :question: Click on the parameters passed to method calls of the Random instance in the following code
      :iscode:
      
      :click-incorrect:Random:endclick: :click-incorrect:rand:endclick: = :click-incorrect:new Random():endclick:;
      :click-incorrect:int:endclick: :click-incorrect:flippedCoin:endclick: = :click-incorrect:rand:endclick::click-incorrect:.nextInt:endclick:(:click-correct:2:endclick:);
      :click-incorrect:int:endclick: :click-incorrect:playingCard:endclick: = :click-incorrect:rand:endclick::click-incorrect:.nextInt:endclick:(:click-correct:52:endclick:);

.. activecode:: ac-objuse-we5-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }