WrClasses-WE4-P2
----------------------

.. qnum::
   :prefix: Q
   :start: 51

    
.. topic:: Subgoals for Writing a Class 4/4

   1. Name it 


   2. Differentiate class-level (static) vs. instance/object-level variables  


   3. Differentiate class-level (static) vs. instance/object behaviors/methods 
   

   4. Define class variables (static) as needed '
   
      A. Name 
      B. Data Type 
      C. public / private / final 
      
      
   5. Define instance variables (that you want to be interrelated)  

      A. Name 
      B. Data Type 
      C. private 
      
      
   6. Create constructor (behavior) that creates initial state of object  

      A. public
      B. Same name as class
      C. No return type
      D. Default - no parameters
      E. Logic - initialize all variables
      F. Repeat as needed, adding parameters 
      
   
   7.  Create 1 accessor and 1 mutator behaviors per attribute

      A. Accessors 

         a. Name is get_<attr_name> 
         b. Public 
         c. Return type same data type as attribute
         d. No parameters 
         e. Logic - return value

      B. Mutators 
      
         a. Name is set_<attr_name>
         b. Public
         c. Return type is void 
         d. Parameter is same data type as attribute
         e. Logic validates input parameter and sets attribute value 
         
      
   8. Write toString method
   
      A. public
      B. Returns String
      C. No parameters
      D. Logic - convert needed attributes to a format that can be printed 
   
   9. Write equals method 
   
      A. public 
      B. Returns boolean
      C. Parameter - instance of the class
      D. Logic - compare attributes for equity
      
   10. Create additional methods as needed 
   

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: Classes-WE4-P2

   .. clickablearea:: ca-Classes-WE4-P2-51
      :question: Identify all constructors.
      :iscode:

      :click-incorrect:/* Coins Class */:endclick:
      :click-incorrect:public class Coins:endclick: {
         :click-incorrect:private int quarters;:endclick:
         :click-incorrect:private int dimes;:endclick:
         :click-incorrect:private int nickels;:endclick:
         :click-incorrect:private int pennies;:endclick:

         public :click-correct:Coins:endclick:(:click-incorrect:int newQuarters, int newDimes, int newNickels, int newPennies:endclick:) {
            setQuarters( newQuarters );
            setDimes( newDimes );
            setNickels( newNickels );
            setPennies( newPennies );
         }

         public :click-correct:Coins:endclick:( ) {
            setQuarters( 0 );
            setDimes( 0 );
            setNickels( 0 );
            setPennies( 0 );
         }

         public int :click-incorrect:getQuarters:endclick:( )   {
            :click-incorrect:return quarters;:endclick:
         }

         public void :click-incorrect:setQuarters:endclick:( :click-incorrect:int newQuarters:endclick: ) {
            if ( newQuarters >= 0 )
               quarters = newQuarters;
            else {
               System.out.println( "The number of quarters cannot be negative." );
               System.out.println( "Value not changed." );
            }
         }

         public int :click-incorrect:getDimes:endclick:( )  {
            :click-incorrect:return dimes;:endclick:
         }

         public void :click-incorrect:setDimes:endclick:( :click-incorrect:int newDimes:endclick: ) {
            if ( newDimes >= 0 )
               dimes = newDimes;
            else {
               System.out.println( "The number of dimes cannot be negative." );
               System.out.println( "Value not changed." );
            }
         }

         public int :click-incorrect:getNickels:endclick:( ) {
            :click-incorrect:return nickels;:endclick:
         }

         public void :click-incorrect:setNickels:endclick:( :click-incorrect:int newNickels:endclick: )   {
            if ( newNickels >= 0 )
               nickels = newNickels;
            else {
               System.out.println( "The number of nickels cannot be negative." );
               System.out.println( "Value not changed." );
            }
         }

         public int :click-incorrect:getPennies:endclick:( ) {
            :click-incorrect:return pennies;:endclick:
         }

         public void :click-incorrect:setPennies:endclick:( :click-incorrect:int newPennies:endclick: )  {
            if ( newPennies >= 0 )
               pennies = newPennies;
            else {
               System.out.println( "The number of pennies cannot be negative." );
               System.out.println( "Value not changed." );
            }
         }

         public String toString( ) {
            :click-incorrect:return( "quarters: " + quarters + "; dimes: " + dimes
               + "; nickels: " + nickels + "; pennies:" + pennies );:endclick:
         } 

         public boolean equals( Coins c )  {
            :click-incorrect:return ( quarters == c.quarters && dimes == c.dimes
               && nickels == c.nickels && pennies == c.pennies );:endclick:
         }

         private double moneyFromQuarters( )  {
            :click-incorrect:return ( quarters * .25 );:endclick:
         }

         private double moneyFromDimes( )  {
            :click-incorrect:return ( dimes * .1 );:endclick:
         } 

         private double moneyFromNickels( )  {
            :click-incorrect:return ( nickels * .05 );:endclick:
         }

         private double moneyFromPennies( ) {
            :click-incorrect:return ( pennies * .01 );:endclick:
         }

         public double :click-incorrect:total:endclick:( ) {
            :click-incorrect:return moneyFromQuarters + 
               moneyFromDimes + 
               moneyFromNickels + 
               moneyFromPennies;:endclick:
         }

         public double :click-incorrect:convert:endclick:( :click-incorrect:double rate:endclick: ) {
            :click-incorrect:return total * rate;:endclick:
         }
      }

   .. clickablearea:: ca-Classes-WE4-P2-52
      :question: Identify all accessor/getter methods.
      :iscode:

      :click-incorrect:/* Coins Class */:endclick:
      :click-incorrect:public class Coins:endclick: {
         :click-incorrect:private int quarters;:endclick:
         :click-incorrect:private int dimes;:endclick:
         :click-incorrect:private int nickels;:endclick:
         :click-incorrect:private int pennies;:endclick:

         public :click-incorrect:Coins:endclick:(:click-incorrect:int newQuarters, int newDimes, int newNickels, int newPennies:endclick:) {
            setQuarters( newQuarters );
            setDimes( newDimes );
            setNickels( newNickels );
            setPennies( newPennies );
         }

         public :click-incorrect:Coins:endclick:( ) {
            setQuarters( 0 );
            setDimes( 0 );
            setNickels( 0 );
            setPennies( 0 );
         }

         public int :click-correct:getQuarters:endclick:( )   {
            :click-incorrect:return quarters;:endclick:
         }

         public void :click-incorrect:setQuarters:endclick:( :click-incorrect:int newQuarters:endclick: ) {
            if ( newQuarters >= 0 )
               quarters = newQuarters;
            else {
               System.out.println( "The number of quarters cannot be negative." );
               System.out.println( "Value not changed." );
            }
         }

         public int :click-correct:getDimes:endclick:( )  {
            :click-incorrect:return dimes;:endclick:
         }

         public void :click-incorrect:setDimes:endclick:( :click-incorrect:int newDimes:endclick: ) {
            if ( newDimes >= 0 )
               dimes = newDimes;
            else {
               System.out.println( "The number of dimes cannot be negative." );
               System.out.println( "Value not changed." );
            }
         }

         public int :click-correct:getNickels:endclick:( ) {
            :click-incorrect:return nickels;:endclick:
         }

         public void :click-incorrect:setNickels:endclick:( :click-incorrect:int newNickels:endclick: )   {
            if ( newNickels >= 0 )
               nickels = newNickels;
            else {
               System.out.println( "The number of nickels cannot be negative." );
               System.out.println( "Value not changed." );
            }
         }

         public int :click-correct:getPennies:endclick:( ) {
            :click-incorrect:return pennies;:endclick:
         }

         public void :click-incorrect:setPennies:endclick:( :click-incorrect:int newPennies:endclick: )  {
            if ( newPennies >= 0 )
               pennies = newPennies;
            else {
               System.out.println( "The number of pennies cannot be negative." );
               System.out.println( "Value not changed." );
            }
         }

         public String toString( ) {
            :click-incorrect:return( "quarters: " + quarters + "; dimes: " + dimes
               + "; nickels: " + nickels + "; pennies:" + pennies );:endclick:
         } 

         public boolean equals( Coins c )  {
            :click-incorrect:return ( quarters == c.quarters && dimes == c.dimes
               && nickels == c.nickels && pennies == c.pennies );:endclick:
         }

         private double moneyFromQuarters( )  {
            :click-incorrect:return ( quarters * .25 );:endclick:
         }

         private double moneyFromDimes( )  {
            :click-incorrect:return ( dimes * .1 );:endclick:
         } 

         private double moneyFromNickels( )  {
            :click-incorrect:return ( nickels * .05 );:endclick:
         }

         private double moneyFromPennies( ) {
            :click-incorrect:return ( pennies * .01 );:endclick:
         }

         public double :click-incorrect:total:endclick:( ) {
            :click-incorrect:return moneyFromQuarters + 
               moneyFromDimes + 
               moneyFromNickels + 
               moneyFromPennies;:endclick:
         }

         public double :click-incorrect:convert:endclick:( :click-incorrect:double rate:endclick: ) {
            :click-incorrect:return total * rate;:endclick:
         }
      }

   .. clickablearea:: ca-Classes-WE4-P2-53
      :question: Identify all mutator/setter methods.
      :iscode:

      :click-incorrect:/* Coins Class */:endclick:
      :click-incorrect:public class Coins:endclick: {
         :click-incorrect:private int quarters;:endclick:
         :click-incorrect:private int dimes;:endclick:
         :click-incorrect:private int nickels;:endclick:
         :click-incorrect:private int pennies;:endclick:

         public :click-incorrect:Coins:endclick:(:click-incorrect:int newQuarters, int newDimes, int newNickels, int newPennies:endclick:) {
            setQuarters( newQuarters );
            setDimes( newDimes );
            setNickels( newNickels );
            setPennies( newPennies );
         }

         public :click-incorrect:Coins:endclick:( ) {
            setQuarters( 0 );
            setDimes( 0 );
            setNickels( 0 );
            setPennies( 0 );
         }

         public int :click-incorrect:getQuarters:endclick:( )   {
            :click-incorrect:return quarters;:endclick:
         }

         public void :click-correct:setQuarters:endclick:( :click-incorrect:int newQuarters:endclick: ) {
            if ( newQuarters >= 0 )
               quarters = newQuarters;
            else {
               System.out.println( "The number of quarters cannot be negative." );
               System.out.println( "Value not changed." );
            }
         }

         public int :click-incorrect:getDimes:endclick:( )  {
            :click-incorrect:return dimes;:endclick:
         }

         public void :click-correct:setDimes:endclick:( :click-incorrect:int newDimes:endclick: ) {
            if ( newDimes >= 0 )
               dimes = newDimes;
            else {
               System.out.println( "The number of dimes cannot be negative." );
               System.out.println( "Value not changed." );
            }
         }

         public int :click-incorrect:getNickels:endclick:( ) {
            :click-incorrect:return nickels;:endclick:
         }

         public void :click-correct:setNickels:endclick:( :click-incorrect:int newNickels:endclick: )   {
            if ( newNickels >= 0 )
               nickels = newNickels;
            else {
               System.out.println( "The number of nickels cannot be negative." );
               System.out.println( "Value not changed." );
            }
         }

         public int :click-incorrect:getPennies:endclick:( ) {
            :click-incorrect:return pennies;:endclick:
         }

         public void :click-correct:setPennies:endclick:( :click-incorrect:int newPennies:endclick: )  {
            if ( newPennies >= 0 )
               pennies = newPennies;
            else {
               System.out.println( "The number of pennies cannot be negative." );
               System.out.println( "Value not changed." );
            }
         }

         public String toString( ) {
            :click-incorrect:return( "quarters: " + quarters + "; dimes: " + dimes
               + "; nickels: " + nickels + "; pennies:" + pennies );:endclick:
         } 

         public boolean equals( Coins c )  {
            :click-incorrect:return ( quarters == c.quarters && dimes == c.dimes
               && nickels == c.nickels && pennies == c.pennies );:endclick:
         }

         private double moneyFromQuarters( )  {
            :click-incorrect:return ( quarters * .25 );:endclick:
         }

         private double moneyFromDimes( )  {
            :click-incorrect:return ( dimes * .1 );:endclick:
         } 

         private double moneyFromNickels( )  {
            :click-incorrect:return ( nickels * .05 );:endclick:
         }

         private double moneyFromPennies( ) {
            :click-incorrect:return ( pennies * .01 );:endclick:
         }

         public double :click-incorrect:total:endclick:( ) {
            :click-incorrect:return moneyFromQuarters + 
               moneyFromDimes + 
               moneyFromNickels + 
               moneyFromPennies;:endclick:
         }

         public double :click-incorrect:convert:endclick:( :click-incorrect:double rate:endclick: ) {
            :click-incorrect:return total * rate;:endclick:
         }
      }

   .. clickablearea:: ca-Classes-WE4-P2-54
      :question: Identify the attributes.
      :iscode:

      :click-incorrect:/* Coins Class */:endclick:
      :click-incorrect:public class Coins:endclick: {
         :click-correct:private int quarters;:endclick:
         :click-correct:private int dimes;:endclick:
         :click-correct:private int nickels;:endclick:
         :click-correct:private int pennies;:endclick:

         public :click-incorrect:Coins:endclick:(:click-incorrect:int newQuarters, int newDimes, int newNickels, int newPennies:endclick:) {
            setQuarters( newQuarters );
            setDimes( newDimes );
            setNickels( newNickels );
            setPennies( newPennies );
         }

         public :click-incorrect:Coins:endclick:( ) {
            setQuarters( 0 );
            setDimes( 0 );
            setNickels( 0 );
            setPennies( 0 );
         }

         public int :click-incorrect:getQuarters:endclick:( )   {
            :click-incorrect:return quarters;:endclick:
         }

         public void :click-incorrect:setQuarters:endclick:( :click-incorrect:int newQuarters:endclick: ) {
            if ( newQuarters >= 0 )
               quarters = newQuarters;
            else {
               System.out.println( "The number of quarters cannot be negative." );
               System.out.println( "Value not changed." );
            }
         }

         public int :click-incorrect:getDimes:endclick:( )  {
            :click-incorrect:return dimes;:endclick:
         }

         public void :click-incorrect:setDimes:endclick:( :click-incorrect:int newDimes:endclick: ) {
            if ( newDimes >= 0 )
               dimes = newDimes;
            else {
               System.out.println( "The number of dimes cannot be negative." );
               System.out.println( "Value not changed." );
            }
         }

         public int :click-incorrect:getNickels:endclick:( ) {
            :click-incorrect:return nickels;:endclick:
         }

         public void :click-incorrect:setNickels:endclick:( :click-incorrect:int newNickels:endclick: )   {
            if ( newNickels >= 0 )
               nickels = newNickels;
            else {
               System.out.println( "The number of nickels cannot be negative." );
               System.out.println( "Value not changed." );
            }
         }

         public int :click-incorrect:getPennies:endclick:( ) {
            :click-incorrect:return pennies;:endclick:
         }

         public void :click-incorrect:setPennies:endclick:( :click-incorrect:int newPennies:endclick: )  {
            if ( newPennies >= 0 )
               pennies = newPennies;
            else {
               System.out.println( "The number of pennies cannot be negative." );
               System.out.println( "Value not changed." );
            }
         }

         public String toString( ) {
            :click-incorrect:return( "quarters: " + quarters + "; dimes: " + dimes
               + "; nickels: " + nickels + "; pennies:" + pennies );:endclick:
         } 

         public boolean equals( Coins c )  {
            :click-incorrect:return ( quarters == c.quarters && dimes == c.dimes
               && nickels == c.nickels && pennies == c.pennies );:endclick:
         }

         private double moneyFromQuarters( )  {
            :click-incorrect:return ( quarters * .25 );:endclick:
         }

         private double moneyFromDimes( )  {
            :click-incorrect:return ( dimes * .1 );:endclick:
         } 

         private double moneyFromNickels( )  {
            :click-incorrect:return ( nickels * .05 );:endclick:
         }

         private double moneyFromPennies( ) {
            :click-incorrect:return ( pennies * .01 );:endclick:
         }

         public double :click-incorrect:total:endclick:( ) {
            :click-incorrect:return moneyFromQuarters + 
               moneyFromDimes + 
               moneyFromNickels + 
               moneyFromPennies;:endclick:
         }

         public double :click-incorrect:convert:endclick:( :click-incorrect:double rate:endclick: ) {
            :click-incorrect:return total * rate;:endclick:
         }
      }

   .. clickablearea:: ca-Classes-WE4-P2-55
      :question: Identify the helper or auxiliary methods.
      :iscode:

      :click-incorrect:/* Coins Class */:endclick:
      :click-incorrect:public class Coins:endclick: {
         :click-incorrect:private int quarters;:endclick:
         :click-incorrect:private int dimes;:endclick:
         :click-incorrect:private int nickels;:endclick:
         :click-incorrect:private int pennies;:endclick:

         public :click-incorrect:Coins:endclick:(:click-incorrect:int newQuarters, int newDimes, int newNickels, int newPennies:endclick:) {
            setQuarters( newQuarters );
            setDimes( newDimes );
            setNickels( newNickels );
            setPennies( newPennies );
         }

         public :click-incorrect:Coins:endclick:( ) {
            setQuarters( 0 );
            setDimes( 0 );
            setNickels( 0 );
            setPennies( 0 );
         }

         public int :click-incorrect:getQuarters:endclick:( )   {
            :click-incorrect:return quarters;:endclick:
         }

         public void :click-incorrect:setQuarters:endclick:( :click-incorrect:int newQuarters:endclick: ) {
            if ( newQuarters >= 0 )
               quarters = newQuarters;
            else {
               System.out.println( "The number of quarters cannot be negative." );
               System.out.println( "Value not changed." );
            }
         }

         public int :click-incorrect:getDimes:endclick:( )  {
            :click-incorrect:return dimes;:endclick:
         }

         public void :click-incorrect:setDimes:endclick:( :click-incorrect:int newDimes:endclick: ) {
            if ( newDimes >= 0 )
               dimes = newDimes;
            else {
               System.out.println( "The number of dimes cannot be negative." );
               System.out.println( "Value not changed." );
            }
         }

         public int :click-incorrect:getNickels:endclick:( ) {
            :click-incorrect:return nickels;:endclick:
         }

         public void :click-incorrect:setNickels:endclick:( :click-incorrect:int newNickels:endclick: )   {
            if ( newNickels >= 0 )
               nickels = newNickels;
            else {
               System.out.println( "The number of nickels cannot be negative." );
               System.out.println( "Value not changed." );
            }
         }

         public int :click-incorrect:getPennies:endclick:( ) {
            :click-incorrect:return pennies;:endclick:
         }

         public void :click-incorrect:setPennies:endclick:( :click-incorrect:int newPennies:endclick: )  {
            if ( newPennies >= 0 )
               pennies = newPennies;
            else {
               System.out.println( "The number of pennies cannot be negative." );
               System.out.println( "Value not changed." );
            }
         }

         public String toString( ) {
            :click-incorrect:return( "quarters: " + quarters + "; dimes: " + dimes
               + "; nickels: " + nickels + "; pennies:" + pennies );:endclick:
         } 

         public boolean equals( Coins c )  {
            :click-incorrect:return ( quarters == c.quarters && dimes == c.dimes
               && nickels == c.nickels && pennies == c.pennies );:endclick:
         }

         private double moneyFromQuarters( )  {
            :click-incorrect:return ( quarters * .25 );:endclick:
         }

         private double moneyFromDimes( )  {
            :click-incorrect:return ( dimes * .1 );:endclick:
         } 

         private double moneyFromNickels( )  {
            :click-incorrect:return ( nickels * .05 );:endclick:
         }

         private double moneyFromPennies( ) {
            :click-incorrect:return ( pennies * .01 );:endclick:
         }

         public double :click-correct:total:endclick:( ) {
            :click-incorrect:return moneyFromQuarters + 
               moneyFromDimes + 
               moneyFromNickels + 
               moneyFromPennies;:endclick:
         }

         public double :click-correct:convert:endclick:( :click-incorrect:double rate:endclick: ) {
            :click-incorrect:return total * rate;:endclick:
         }
      }
      
   
   
.. activecode:: ac-classes-we4-p2
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }