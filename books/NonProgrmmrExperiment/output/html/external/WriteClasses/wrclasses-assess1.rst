Assessment: Writing Classes 1
---------------------------------------------

.. qnum::
   :prefix: Q
   :start: 1

    
.. topic:: Subgoals for Writing a Class 3/4

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

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. timed:: assess-wrclasses-1
   :nofeedback:

   .. mchoice:: assess-wrclasses-1-1
      :multiple_answers:
      :answer_a: public Coins( )
      :answer_b: public Coins(int newQuarters, int newDimes, int newNickels, int newPennies)
      :answer_c: public double total( )
      :answer_d: public double convert( double rate )
      :answer_e: public NewCoins()
      :correct: a, b
      
      Consider the following class defintion.
   
      .. code-block:: java
      
         /* Coins Class */
         public class Coins {
            private int quarters;
            private int dimes;
            private int nickels;
            private int pennies;

            public Coins(int newQuarters, int newDimes, int newNickels, int newPennies) {
               setQuarters( newQuarters );
               setDimes( newDimes );
               setNickels( newNickels );
               setPennies( newPennies );
            }

            public Coins( ) {
               setQuarters( 0 );
               setDimes( 0 );
               setNickels( 0 );
               setPennies( 0 );
            }

            public int getQuarters( )   {
               return quarters;
            }

            public void setQuarters( int newQuarters ) {
               if ( newQuarters >= 0 )
                  quarters = newQuarters;
               else {
                  System.out.println( "The number of quarters cannot be negative." );
                  System.out.println( "Value not changed." );
               }
            }

            public int getDimes( )  {
               return dimes;
            }

            public void setDimes( int newDimes ) {
               if ( newDimes >= 0 )
                  dimes = newDimes;
               else {
                  System.out.println( "The number of dimes cannot be negative." );
                  System.out.println( "Value not changed." );
               }
            }

            public int getNickels( ) {
               return nickels;
            }

            public void setNickels( int newNickels )   {
               if ( newNickels >= 0 )
                  nickels = newNickels;
               else {
                  System.out.println( "The number of nickels cannot be negative." );
                  System.out.println( "Value not changed." );
               }
            }

            public int getPennies( ) {
               return pennies;
            }

            public void setPennies( int newPennies )  {
               if ( newPennies >= 0 )
                  pennies = newPennies;
               else {
                  System.out.println( "The number of pennies cannot be negative." );
                  System.out.println( "Value not changed." );
               }
            }

            public String toString( ) {
               return( "quarters: " + quarters + "; dimes: " + dimes
                  + "; nickels: " + nickels + "; pennies:" + pennies );
            } 

            public boolean equals( Coins c )  {
               return ( quarters == c.quarters && dimes == c.dimes
                  && nickels == c.nickels && pennies == c.pennies );
            }

            private double moneyFromQuarters( )  {
               return ( quarters * .25 );
            }

            private double moneyFromDimes( )  {
               return ( dimes * .1 );
            } 

            private double moneyFromNickels( )  {
               return ( nickels * .05 );
            }

            private double moneyFromPennies( ) {
               return ( pennies * .01 );
            }

            public double total( ) {
               return moneyFromQuarters + moneyFromDimes + moneyFromNickels + moneyFromPennies;
            }

            public double convert( double rate ) {
               return total * rate;
            }
         }
         
      Identify all the constructors from the given class definition above. Choose all that apply.

   .. mchoice:: assess-wrclasses-1-2
      :answer_a: Coins
      :answer_b: getQuarters, getDimes, getNickels, getPennies
      :answer_c: setQuarters, setDimes, setNickels, setPennies
      :answer_d: moneyFromQuarters, moneyFromDimes, moneyFromNickels, moneyFromPennies
      :answer_e: total, convert
      :correct: b
      
      Consider the following class definition.
   
      .. code-block:: java
      
         /* Coins Class */
         public class Coins {
            private int quarters;
            private int dimes;
            private int nickels;
            private int pennies;

            public Coins(int newQuarters, int newDimes, int newNickels, int newPennies) {
               setQuarters( newQuarters );
               setDimes( newDimes );
               setNickels( newNickels );
               setPennies( newPennies );
            }

            public Coins( ) {
               setQuarters( 0 );
               setDimes( 0 );
               setNickels( 0 );
               setPennies( 0 );
            }

            public int getQuarters( )   {
               return quarters;
            }

            public void setQuarters( int newQuarters ) {
               if ( newQuarters >= 0 )
                  quarters = newQuarters;
               else {
                  System.out.println( "The number of quarters cannot be negative." );
                  System.out.println( "Value not changed." );
               }
            }

            public int getDimes( )  {
               return dimes;
            }

            public void setDimes( int newDimes ) {
               if ( newDimes >= 0 )
                  dimes = newDimes;
               else {
                  System.out.println( "The number of dimes cannot be negative." );
                  System.out.println( "Value not changed." );
               }
            }

            public int getNickels( ) {
               return nickels;
            }

            public void setNickels( int newNickels )   {
               if ( newNickels >= 0 )
                  nickels = newNickels;
               else {
                  System.out.println( "The number of nickels cannot be negative." );
                  System.out.println( "Value not changed." );
               }
            }

            public int getPennies( ) {
               return pennies;
            }

            public void setPennies( int newPennies )  {
               if ( newPennies >= 0 )
                  pennies = newPennies;
               else {
                  System.out.println( "The number of pennies cannot be negative." );
                  System.out.println( "Value not changed." );
               }
            }

            public String toString( ) {
               return( "quarters: " + quarters + "; dimes: " + dimes
                  + "; nickels: " + nickels + "; pennies:" + pennies );
            } 

            public boolean equals( Coins c )  {
               return ( quarters == c.quarters && dimes == c.dimes
                  && nickels == c.nickels && pennies == c.pennies );
            }

            private double moneyFromQuarters( )  {
               return ( quarters * .25 );
            }

            private double moneyFromDimes( )  {
               return ( dimes * .1 );
            } 

            private double moneyFromNickels( )  {
               return ( nickels * .05 );
            }

            private double moneyFromPennies( ) {
               return ( pennies * .01 );
            }

            public double total( ) {
               return moneyFromQuarters + moneyFromDimes + moneyFromNickels + moneyFromPennies;
            }

            public double convert( double rate ) {
               return total * rate;
            }
         }
         
      Identify the accessor/getter methods.

   .. mchoice:: assess-wrclasses-1-3
      :answer_a: Coins
      :answer_b: getQuarters, getDimes, getNickels, getPennies
      :answer_c: setQuarters, setDimes, setNickels, setPennies
      :answer_d: moneyFromQuarters, moneyFromDimes, moneyFromNickels, moneyFromPennies
      :answer_e: total, convert
      :correct: c
      
      Consider the following class definition.
   
      .. code-block:: java
      
         /* Coins Class */
         public class Coins {
            private int quarters;
            private int dimes;
            private int nickels;
            private int pennies;

            public Coins(int newQuarters, int newDimes, int newNickels, int newPennies) {
               setQuarters( newQuarters );
               setDimes( newDimes );
               setNickels( newNickels );
               setPennies( newPennies );
            }

            public Coins( ) {
               setQuarters( 0 );
               setDimes( 0 );
               setNickels( 0 );
               setPennies( 0 );
            }

            public int getQuarters( )   {
               return quarters;
            }

            public void setQuarters( int newQuarters ) {
               if ( newQuarters >= 0 )
                  quarters = newQuarters;
               else {
                  System.out.println( "The number of quarters cannot be negative." );
                  System.out.println( "Value not changed." );
               }
            }

            public int getDimes( )  {
               return dimes;
            }

            public void setDimes( int newDimes ) {
               if ( newDimes >= 0 )
                  dimes = newDimes;
               else {
                  System.out.println( "The number of dimes cannot be negative." );
                  System.out.println( "Value not changed." );
               }
            }

            public int getNickels( ) {
               return nickels;
            }

            public void setNickels( int newNickels )   {
               if ( newNickels >= 0 )
                  nickels = newNickels;
               else {
                  System.out.println( "The number of nickels cannot be negative." );
                  System.out.println( "Value not changed." );
               }
            }

            public int getPennies( ) {
               return pennies;
            }

            public void setPennies( int newPennies )  {
               if ( newPennies >= 0 )
                  pennies = newPennies;
               else {
                  System.out.println( "The number of pennies cannot be negative." );
                  System.out.println( "Value not changed." );
               }
            }

            public String toString( ) {
               return( "quarters: " + quarters + "; dimes: " + dimes
                  + "; nickels: " + nickels + "; pennies:" + pennies );
            } 

            public boolean equals( Coins c )  {
               return ( quarters == c.quarters && dimes == c.dimes
                  && nickels == c.nickels && pennies == c.pennies );
            }

            private double moneyFromQuarters( )  {
               return ( quarters * .25 );
            }

            private double moneyFromDimes( )  {
               return ( dimes * .1 );
            } 

            private double moneyFromNickels( )  {
               return ( nickels * .05 );
            }

            private double moneyFromPennies( ) {
               return ( pennies * .01 );
            }

            public double total( ) {
               return moneyFromQuarters + moneyFromDimes + moneyFromNickels + moneyFromPennies;
            }

            public double convert( double rate ) {
               return total * rate;
            }
         }
         
      Identify the mutator/setter methods.

   .. mchoice:: assess-wrclasses-1-4
      :answer_a: quarters, dimes, nickels, pennies
      :answer_b: getQuarters, getDimes, getNickels, getPennies
      :answer_c: setQuarters, setDimes, setNickels, setPennies
      :answer_d: moneyFromQuarters, moneyFromDimes, moneyFromNickels, moneyFromPennies
      :answer_e: total, convert
      :correct: a
      
      Consider the following class definition.
   
      .. code-block:: java
      
         /* Coins Class */
         public class Coins {
            private int quarters;
            private int dimes;
            private int nickels;
            private int pennies;

            public Coins(int newQuarters, int newDimes, int newNickels, int newPennies) {
               setQuarters( newQuarters );
               setDimes( newDimes );
               setNickels( newNickels );
               setPennies( newPennies );
            }

            public Coins( ) {
               setQuarters( 0 );
               setDimes( 0 );
               setNickels( 0 );
               setPennies( 0 );
            }

            public int getQuarters( )   {
               return quarters;
            }

            public void setQuarters( int newQuarters ) {
               if ( newQuarters >= 0 )
                  quarters = newQuarters;
               else {
                  System.out.println( "The number of quarters cannot be negative." );
                  System.out.println( "Value not changed." );
               }
            }

            public int getDimes( )  {
               return dimes;
            }

            public void setDimes( int newDimes ) {
               if ( newDimes >= 0 )
                  dimes = newDimes;
               else {
                  System.out.println( "The number of dimes cannot be negative." );
                  System.out.println( "Value not changed." );
               }
            }

            public int getNickels( ) {
               return nickels;
            }

            public void setNickels( int newNickels )   {
               if ( newNickels >= 0 )
                  nickels = newNickels;
               else {
                  System.out.println( "The number of nickels cannot be negative." );
                  System.out.println( "Value not changed." );
               }
            }

            public int getPennies( ) {
               return pennies;
            }

            public void setPennies( int newPennies )  {
               if ( newPennies >= 0 )
                  pennies = newPennies;
               else {
                  System.out.println( "The number of pennies cannot be negative." );
                  System.out.println( "Value not changed." );
               }
            }

            public String toString( ) {
               return( "quarters: " + quarters + "; dimes: " + dimes
                  + "; nickels: " + nickels + "; pennies:" + pennies );
            } 

            public boolean equals( Coins c )  {
               return ( quarters == c.quarters && dimes == c.dimes
                  && nickels == c.nickels && pennies == c.pennies );
            }

            private double moneyFromQuarters( )  {
               return ( quarters * .25 );
            }

            private double moneyFromDimes( )  {
               return ( dimes * .1 );
            } 

            private double moneyFromNickels( )  {
               return ( nickels * .05 );
            }

            private double moneyFromPennies( ) {
               return ( pennies * .01 );
            }

            public double total( ) {
               return moneyFromQuarters + moneyFromDimes + moneyFromNickels + moneyFromPennies;
            }

            public double convert( double rate ) {
               return total * rate;
            }
         }
         
      Which of the choices lists ``attributes`` of the given class?

   .. mchoice:: assess-wrclasses-1-5
      :answer_a: Coins
      :answer_b: getQuarters, getDimes, getNickels, getPennies
      :answer_c: setQuarters, setDimes, setNickels, setPennies
      :answer_d: moneyFromQuarters, moneyFromDimes, moneyFromNickels, moneyFromPennies
      :answer_e: total, convert
      :correct: e
      
      Consider the following class definiton.
   
      .. code-block:: java
      
         /* Coins Class */
         public class Coins {
            private int quarters;
            private int dimes;
            private int nickels;
            private int pennies;

            public Coins(int newQuarters, int newDimes, int newNickels, int newPennies) {
               setQuarters( newQuarters );
               setDimes( newDimes );
               setNickels( newNickels );
               setPennies( newPennies );
            }

            public Coins( ) {
               setQuarters( 0 );
               setDimes( 0 );
               setNickels( 0 );
               setPennies( 0 );
            }

            public int getQuarters( )   {
               return quarters;
            }

            public void setQuarters( int newQuarters ) {
               if ( newQuarters >= 0 )
                  quarters = newQuarters;
               else {
                  System.out.println( "The number of quarters cannot be negative." );
                  System.out.println( "Value not changed." );
               }
            }

            public int getDimes( )  {
               return dimes;
            }

            public void setDimes( int newDimes ) {
               if ( newDimes >= 0 )
                  dimes = newDimes;
               else {
                  System.out.println( "The number of dimes cannot be negative." );
                  System.out.println( "Value not changed." );
               }
            }

            public int getNickels( ) {
               return nickels;
            }

            public void setNickels( int newNickels )   {
               if ( newNickels >= 0 )
                  nickels = newNickels;
               else {
                  System.out.println( "The number of nickels cannot be negative." );
                  System.out.println( "Value not changed." );
               }
            }

            public int getPennies( ) {
               return pennies;
            }

            public void setPennies( int newPennies )  {
               if ( newPennies >= 0 )
                  pennies = newPennies;
               else {
                  System.out.println( "The number of pennies cannot be negative." );
                  System.out.println( "Value not changed." );
               }
            }

            public String toString( ) {
               return( "quarters: " + quarters + "; dimes: " + dimes
                  + "; nickels: " + nickels + "; pennies:" + pennies );
            } 

            public boolean equals( Coins c )  {
               return ( quarters == c.quarters && dimes == c.dimes
                  && nickels == c.nickels && pennies == c.pennies );
            }

            private double moneyFromQuarters( )  {
               return ( quarters * .25 );
            }

            private double moneyFromDimes( )  {
               return ( dimes * .1 );
            } 

            private double moneyFromNickels( )  {
               return ( nickels * .05 );
            }

            private double moneyFromPennies( ) {
               return ( pennies * .01 );
            }

            public double total( ) {
               return moneyFromQuarters + moneyFromDimes + moneyFromNickels + moneyFromPennies;
            }

            public double convert( double rate ) {
               return total * rate;
            }
         }
      
      Identify the helper or auxiliary methods.