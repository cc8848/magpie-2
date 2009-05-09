﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Magpie.Compilation
{
    public class DeclComparer : IDeclVisitor<bool>
    {
        public static bool TypesMatch(Decl[] parameters, Decl[] arguments)
        {
            if (parameters.Length != arguments.Length) return false;

            for (int i = 0; i < parameters.Length; i++)
            {
                if (!TypesMatch(parameters[i], arguments[i])) return false;
            }

            return true;
        }

        public static bool TypesMatch(Decl parameter, Decl argument)
        {
            if (parameter is AnyType) return true;

            return argument.Accept(new DeclComparer(parameter));
        }

        #region IDeclVisitor Members

        bool IDeclVisitor<bool>.Visit(AnyType decl)
        {
            return true;
        }

        bool IDeclVisitor<bool>.Visit(AtomicDecl decl)
        {
            // there is a single instance of each atomic type, so they must match exactly
            return ReferenceEquals(mParam, decl);
        }

        bool IDeclVisitor<bool>.Visit(ArrayType decl)
        {
            ArrayType array = mParam as ArrayType;

            if (array == null) return false;

            // mutability must match
            //### bob: are there cases where we want to let this slide?
            //         can you pass a mutable array everywhere an immutable one is allowed?
            if (decl.IsMutable != array.IsMutable) return false;

            // element type must match
            return TypesMatch(decl.ElementType, array.ElementType);
        }

        bool IDeclVisitor<bool>.Visit(FuncType decl)
        {
            FuncType paramFunc = mParam as FuncType;

            if (paramFunc == null) return false;

            // args must match
            if (paramFunc.Parameters.Count != decl.Parameters.Count) return false;

            for (int i = 0; i < paramFunc.Parameters.Count; i++)
            {
                if (!TypesMatch(paramFunc.Parameters[i].Type, decl.Parameters[i].Type))
                {
                    return false;
                }
            }

            // return type must match
            return TypesMatch(paramFunc.Return, decl.Return);
        }

        bool IDeclVisitor<bool>.Visit(NamedType decl)
        {
            NamedType named = mParam as NamedType;
            if (named == null) return false;

            //### bob: should this be checking the qualified name?
            if (named.Name != decl.Name) return false;

            // the type args must match
            if (named.TypeArgs.Length != decl.TypeArgs.Length) return false;
            return TypesMatch(named.TypeArgs, decl.TypeArgs);
        }

        bool IDeclVisitor<bool>.Visit(TupleType decl)
        {
            TupleType paramTuple = mParam as TupleType;
            if (paramTuple == null) return false;

            if (paramTuple.Fields.Count != decl.Fields.Count) return false;

            // fields must match
            for (int i = 0; i < paramTuple.Fields.Count; i++)
            {
                if (!TypesMatch(paramTuple.Fields[i], decl.Fields[i]))
                {
                    return false;
                }
            }

            return true;
        }

        #endregion

        private DeclComparer(Decl parameter)
        {
            mParam = parameter;
        }

        private Decl mParam;
    }
}
