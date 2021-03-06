/*
 * The contents of this file are subject to the Mozilla Public License
 * Version 1.0 (the "License"); you may not use this file except in
 * compliance with the License. You may obtain a copy of the License at
 * http://www.mozilla.org/MPL/
 *
 * Software distributed under the License is distributed on an "AS IS"
 * basis, WITHOUT WARRANTY OF ANY KIND, either express or implied. See the
 * License for the specific language governing rights and limitations
 * under the License.
 *
 * The Initial Developer of this code is John Hansen.
 * Portions created by John Hansen are Copyright (C) 2005 John Hansen.
 * All Rights Reserved.
 */


#ifndef __AddrOfExpr_h
#define __AddrOfExpr_h

#ifndef __Expr_h
#include "Expr.h"
#endif

#ifndef __VarTranslator_h
#include "VarTranslator.h"
#endif

class AddrOfExpr : public Expr, public Translatable
{
public:
                AddrOfExpr(int value, int offset, const LexLocation &loc);


        virtual bool		PromiseConstant() const;

        virtual bool		Evaluate(int &value) const;
        virtual Expr*		Clone(Mapping *b) const;

        virtual bool		Contains(int var) const;
        virtual RCX_Value	EmitAny_(Bytecode &b) const;
        virtual RCX_Value	GetStaticEA_() const;
        virtual bool            LValueIsPointer() const;

        void				Translate(int from, int to);
private:
        int				fValue;
        int                             foffset;
};


#endif
