# This is used by GYP to generate platform-specific project files for building
# Magpie. (I.e. on a Mac it will create an XCode project, on Linux a makefile.)
# See README for more.

{
  'target_defaults': {
    'dependencies': [
      'dep/libuv/uv.gyp:libuv'
    ],
    'defines': [
      'PLATFORM="<(OS)"',
    ],
    'include_dirs': [
      'dep/libuv/include',
      'src',
      'src/Base',
      'src/Compiler',
      'src/Memory',
      'src/Platform',
      'src/Syntax',
      'src/VM',
    ],
    'sources': [
      'src/magpie.1',
      'src/Base/Array.h',
      'src/Base/Macros.h',
      'src/Base/MagpieString.cpp',
      'src/Base/MagpieString.h',
      'src/Base/Queue.h',
      'src/Base/Stack.h',
      'src/Compiler/Bytecode.h',
      'src/Compiler/Compiler.cpp',
      'src/Compiler/Compiler.h',
      'src/Compiler/ExprCompiler.cpp',
      'src/Compiler/ExprCompiler.h',
      'src/Compiler/Resolver.cpp',
      'src/Compiler/Resolver.h',
      'src/Memory/ForwardingAddress.h',
      'src/Memory/Managed.cpp',
      'src/Memory/Managed.h',
      'src/Memory/Memory.cpp',
      'src/Memory/Memory.h',
      'src/Memory/RootSource.h',
      'src/Memory/Semispace.cpp',
      'src/Memory/Semispace.h',
      'src/Native/Core.h',
      'src/Native/Core.cpp',
      'src/Native/IO.h',
      'src/Native/IO.cpp',
      'src/Native/Net.h',
      'src/Native/Net.cpp',
      'src/Platform/Environment.h',
      'src/Platform/Environment.cpp',
      'src/Platform/Environment_linux.cpp',
      'src/Platform/Environment_mac.cpp',
      'src/Platform/Environment_win.cpp',
      'src/Platform/Path.h',
      'src/Platform/Path.cpp',
      'src/Platform/Path_posix.cpp',
      'src/Platform/Path_win.cpp',
      'src/Syntax/Ast.cpp',
      'src/Syntax/Ast.generated.h',
      'src/Syntax/Ast.h',
      'src/Syntax/ErrorReporter.cpp',
      'src/Syntax/ErrorReporter.h',
      'src/Syntax/Lexer.cpp',
      'src/Syntax/Lexer.h',
      'src/Syntax/Parser.cpp',
      'src/Syntax/Parser.h',
      'src/Syntax/Token.cpp',
      'src/Syntax/Token.h',
      'src/VM/Fiber.cpp',
      'src/VM/Fiber.h',
      'src/VM/Method.cpp',
      'src/VM/Method.h',
      'src/VM/Module.cpp',
      'src/VM/Module.h',
      'src/VM/Object.cpp',
      'src/VM/Object.h',
      'src/VM/Scheduler.cpp',
      'src/VM/Scheduler.h',
      'src/VM/VM.cpp',
      'src/VM/VM.h',
    ],
    'conditions': [
      ['OS!="linux"', {'sources/': [['exclude', '_linux\\.(cpp|h)$']]}],
      ['OS!="mac"', {'sources/': [['exclude', '_mac\\.(cpp|h)$']]}],
      ['OS!="win"', {'sources/': [['exclude', '_win\\.(cpp|h)$']]}],
      ['OS=="win"', {'sources/': [['exclude', '_posix\\.(cpp|h)$']]}],
    ],
  },
  'targets': [
    {
      'target_name': 'magpie',
      'type': 'executable',
      'sources': [
        'src/main.cpp',
      ],
    },
    {
      'target_name': 'unit_tests',
      'type': 'executable',
      'defines': [ 'UNIT_TEST' ],
      'include_dirs': [
        'src/Test',
      ],
      'sources': [
        'src/Test/ArrayTests.cpp',
        'src/Test/ArrayTests.h',
        'src/Test/LexerTests.cpp',
        'src/Test/LexerTests.h',
        'src/Test/MemoryTests.cpp',
        'src/Test/MemoryTests.h',
        'src/Test/ParserTests.cpp',
        'src/Test/ParserTests.h',
        'src/Test/QueueTests.cpp',
        'src/Test/QueueTests.h',
        'src/Test/StringTests.cpp',
        'src/Test/StringTests.h',
        'src/Test/Test.cpp',
        'src/Test/Test.h',
        'src/Test/TestMain.cpp',
        'src/Test/TokenTests.cpp',
        'src/Test/TokenTests.h',
      ],
    },
  ],
}
