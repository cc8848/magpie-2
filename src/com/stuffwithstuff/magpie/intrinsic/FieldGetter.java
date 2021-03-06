package com.stuffwithstuff.magpie.intrinsic;

import com.stuffwithstuff.magpie.ast.Expr;
import com.stuffwithstuff.magpie.ast.pattern.Pattern;
import com.stuffwithstuff.magpie.interpreter.Callable;
import com.stuffwithstuff.magpie.interpreter.ClassObj;
import com.stuffwithstuff.magpie.interpreter.Context;
import com.stuffwithstuff.magpie.interpreter.Obj;
import com.stuffwithstuff.magpie.interpreter.Scope;

/**
 * Built-in callable that returns the value of a named field.
 */
public class FieldGetter implements Callable {
  public FieldGetter(ClassObj classObj, String name, Scope closure) {
    mName = name;
    mPattern = Pattern.record(Pattern.type(Expr.name(classObj.getName())), Pattern.nothing());
    mClosure = closure;
  }
  
  @Override
  public Obj invoke(Context context, Obj arg) {
    Obj value = arg.getField(0).getField(mName);
    if (value == null) return context.nothing();
    return value;
  }
  
  @Override
  public Pattern getPattern() {
    return mPattern;
  }

  @Override
  public Scope getClosure() {
    return mClosure;
  }
  
  @Override
  public String getDoc() {
    return "Gets the value of the field.";
  }

  private final String mName;
  private final Pattern mPattern;
  private final Scope mClosure;
}
