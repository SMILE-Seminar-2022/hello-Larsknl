package GitHub_Test;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class feedback {
	
   String message = "Hello World";	
   MessageUtil messageUtil = new MessageUtil(message);

   @Test
   public void testPrintMessage() {
      assertEquals(messageUtil.printMessage());
   }
}
#Dies ist ein Test 2